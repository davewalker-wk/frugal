package golang

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"

	"github.com/Workiva/frugal/compiler/generator"
	"github.com/Workiva/frugal/compiler/globals"
	"github.com/Workiva/frugal/compiler/parser"
)

const (
	lang             = "go"
	defaultOutputDir = "gen-go"
)

type Generator struct {
	*generator.BaseGenerator
}

func NewGenerator() generator.SingleFileGenerator {
	return &Generator{&generator.BaseGenerator{}}
}

func (g *Generator) GetOutputDir(dir string, p *parser.Program) string {
	if pkg, ok := p.Namespaces[lang]; ok {
		path := generator.GetPackageComponents(pkg)
		dir = filepath.Join(append([]string{dir}, path...)...)
	} else {
		dir = filepath.Join(dir, p.Name)
	}
	return dir
}

func (g *Generator) DefaultOutputDir() string {
	return defaultOutputDir
}

func (g *Generator) CheckCompile(path string) error {
	if out, err := exec.Command("go", "build", path).CombinedOutput(); err != nil {
		fmt.Println(string(out))
		return err
	}
	return nil
}

func (g *Generator) GenerateFile(name string, outputDir string) (*os.File, error) {
	return g.CreateFile(name, outputDir, lang)
}

func (g *Generator) GenerateDocStringComment(file *os.File) error {
	comment := fmt.Sprintf(
		"// Autogenerated by Frugal Compiler (%s)\n"+
			"// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING",
		globals.Version)

	_, err := file.WriteString(comment)
	return err
}

func (g *Generator) GeneratePackage(file *os.File, p *parser.Program) error {
	pkg, ok := p.Namespaces[lang]
	if ok {
		components := getPackageComponents(pkg)
		pkg = components[len(components)-1]
	} else {
		pkg = p.Name
	}
	_, err := file.WriteString(fmt.Sprintf("package %s", pkg))
	return err
}

func (g *Generator) GenerateImports(file *os.File, p *parser.Program) error {
	imports := "import (\n"
	imports += "\t\"fmt\"\n"
	imports += "\t\"log\"\n\n"
	imports += "\t\"git.apache.org/thrift.git/lib/go/thrift\"\n"
	imports += "\t\"github.com/Workiva/frugal/lib/go\"\n"
	imports += ")"
	_, err := file.WriteString(imports)
	return err
}

func (g *Generator) GenerateConstants(file *os.File, name string) error {
	constants := fmt.Sprintf("const delimiter = \"%s\"", globals.TopicDelimiter)
	_, err := file.WriteString(constants)
	return err
}

func (g *Generator) GeneratePublishers(file *os.File, scopes []*parser.Scope) error {
	publishers := ""
	newline := ""
	for _, scope := range scopes {
		publishers += newline
		newline = "\n\n"
		publishers = generatePublisher(publishers, scope)
	}
	_, err := file.WriteString(publishers)
	return err
}

func generatePublisher(publishers string, scope *parser.Scope) string {
	publishers += fmt.Sprintf("type %sPublisher struct {\n", scope.Name)
	publishers += "\tTransport frugal.Transport\n"
	publishers += "\tProtocol  thrift.TProtocol\n"
	publishers += "\tSeqId     int32\n"
	publishers += "}\n\n"

	publishers += fmt.Sprintf("func New%sPublisher(t frugal.TransportFactory, f thrift.TTransportFactory, "+
		"p thrift.TProtocolFactory) *%sPublisher {\n", scope.Name, scope.Name)
	publishers += "\tprovider := frugal.NewProvider(t, f, p)\n"
	publishers += "\ttransport, protocol := provider.New()\n"
	publishers += fmt.Sprintf("\treturn &%sPublisher{\n", scope.Name)
	publishers += "\t\tTransport: transport,\n"
	publishers += "\t\tProtocol:  protocol,\n"
	publishers += "\t\tSeqId:     0,\n"
	publishers += "\t}\n"
	publishers += "}\n\n"

	args := ""
	if len(scope.Prefix.Variables) > 0 {
		for _, variable := range scope.Prefix.Variables {
			args += ", " + variable
		}
		args += " string"
	}

	prefix := ""
	for _, op := range scope.Operations {
		publishers += prefix
		prefix = "\n\n"
		publishers += fmt.Sprintf("func (l *%sPublisher) Publish%s(req *%s%s) error {\n",
			scope.Name, op.Name, op.Param, args)
		publishers += fmt.Sprintf("\top := \"%s\"\n", op.Name)
		publishers += fmt.Sprintf("\tprefix := %s\n", generatePrefixStringTemplate(scope))
		publishers += "\ttopic := fmt.Sprintf(\"%s" + scope.Name + "%s%s\", prefix, delimiter, op)\n"
		publishers += "\tl.Transport.PreparePublish(topic)\n"
		publishers += "\toprot := l.Protocol\n"
		publishers += "\tl.SeqId++\n"
		publishers += "\tif err := oprot.WriteMessageBegin(op, thrift.CALL, l.SeqId); err != nil {\n"
		publishers += "\t\treturn err\n"
		publishers += "\t}\n"
		publishers += "\tif err := req.Write(oprot); err != nil {\n"
		publishers += "\t\treturn err\n"
		publishers += "\t}\n"
		publishers += "\tif err := oprot.WriteMessageEnd(); err != nil {\n"
		publishers += "\t\treturn err\n"
		publishers += "\t}\n"
		publishers += "\treturn oprot.Flush()\n"
		publishers += "}"
	}

	return publishers
}

func generatePrefixStringTemplate(scope *parser.Scope) string {
	if len(scope.Prefix.Variables) == 0 {
		return `""`
	}
	template := "fmt.Sprintf(\""
	template += scope.Prefix.Template()
	template += globals.TopicDelimiter + "\", "
	prefix := ""
	for _, variable := range scope.Prefix.Variables {
		template += prefix + variable
		prefix = ", "
	}
	template += ")"
	return template
}

func (g *Generator) GenerateSubscribers(file *os.File, scopes []*parser.Scope) error {
	subscribers := ""
	newline := ""
	for _, scope := range scopes {
		subscribers += newline
		newline = "\n\n"
		subscribers = generateSubscriber(subscribers, scope)
	}
	_, err := file.WriteString(subscribers)
	return err
}

func generateSubscriber(subscribers string, scope *parser.Scope) string {
	subscribers += fmt.Sprintf("type %sSubscriber struct {\n", scope.Name)
	subscribers += "\tProvider *frugal.Provider\n"
	subscribers += "}\n\n"

	subscribers += fmt.Sprintf("func New%sSubscriber(t frugal.TransportFactory, "+
		"f thrift.TTransportFactory, p thrift.TProtocolFactory) *%sSubscriber {\n", scope.Name, scope.Name)
	subscribers += "\tprovider := frugal.NewProvider(t, f, p)\n"
	subscribers += fmt.Sprintf("\treturn &%sSubscriber{Provider: provider}\n", scope.Name)
	subscribers += "}\n\n"

	args := ""
	prefix := ""
	if len(scope.Prefix.Variables) > 0 {
		for _, variable := range scope.Prefix.Variables {
			args += prefix + variable
			prefix = ", "
		}
		args += " string, "
	}

	prefix = ""
	for _, op := range scope.Operations {
		subscribers += prefix
		prefix = "\n\n"
		subscribers += fmt.Sprintf("func (l *%sSubscriber) Subscribe%s(%shandler func(*%s)) (*frugal.Subscription, error) {\n",
			scope.Name, op.Name, args, op.Param)
		subscribers += fmt.Sprintf("\top := \"%s\"\n", op.Name)
		subscribers += fmt.Sprintf("\tprefix := %s\n", generatePrefixStringTemplate(scope))
		subscribers += "\ttopic := fmt.Sprintf(\"%s" + scope.Name + "%s%s\", prefix, delimiter, op)\n"
		subscribers += "\ttransport, protocol := l.Provider.New()\n"
		subscribers += "\tif err := transport.Subscribe(topic); err != nil {\n"
		subscribers += "\t\treturn nil, err\n"
		subscribers += "\t}\n\n"
		subscribers += "\tsub := frugal.NewSubscription(topic, transport)\n"
		subscribers += "\tgo func() {\n"
		subscribers += "\t\tfor {\n"
		subscribers += fmt.Sprintf("\t\t\treceived, err := l.recv%s(op, protocol)\n", op.Name)
		subscribers += "\t\t\tif err != nil {\n"
		subscribers += "\t\t\t\tif e, ok := err.(thrift.TTransportException); ok && e.TypeId() == thrift.END_OF_FILE {\n"
		subscribers += "\t\t\t\t\treturn\n"
		subscribers += "\t\t\t\t}\n"
		subscribers += "\t\t\t\tlog.Println(\"frugal: error receiving:\", err)\n"
		subscribers += "\t\t\t\tsub.Signal(err)\n"
		subscribers += "\t\t\t\tsub.Unsubscribe()\n"
		subscribers += "\t\t\t\treturn\n"
		subscribers += "\t\t\t}\n"
		subscribers += "\t\t\thandler(received)\n"
		subscribers += "\t\t}\n"
		subscribers += "\t}()\n\n"
		subscribers += "\treturn sub, nil\n"
		subscribers += "}\n\n"

		subscribers += fmt.Sprintf("func (l *%sSubscriber) recv%s(op string, iprot thrift.TProtocol) (*%s, error) {\n",
			scope.Name, op.Name, op.Param)
		subscribers += "\tname, _, _, err := iprot.ReadMessageBegin()\n"
		subscribers += "\tif err != nil {\n"
		subscribers += "\t\treturn nil, err\n"
		subscribers += "\t}\n"
		subscribers += "\tif name != op {\n"
		subscribers += "\t\tiprot.Skip(thrift.STRUCT)\n"
		subscribers += "\t\tiprot.ReadMessageEnd()\n"
		subscribers += "\t\tx9 := thrift.NewTApplicationException(thrift.UNKNOWN_METHOD, \"Unknown function \"+name)\n"
		subscribers += "\t\treturn nil, x9\n"
		subscribers += "\t}\n"
		subscribers += fmt.Sprintf("\treq := &%s{}\n", op.Param)
		subscribers += "\tif err := req.Read(iprot); err != nil {\n"
		subscribers += "\t\treturn nil, err\n"
		subscribers += "\t}\n\n"
		subscribers += "\tiprot.ReadMessageEnd()\n"
		subscribers += "\treturn req, nil\n"
		subscribers += "}"
	}

	return subscribers
}
