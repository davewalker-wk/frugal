package main

import (
	"fmt"
	"net/http"

	"git.apache.org/thrift.git/lib/go/thrift"

	"github.com/Workiva/frugal/examples/go/gen-go/v1/music"
	"github.com/Workiva/frugal/lib/go"
)

// Run an HTTP server
func main() {
	// Set the protocol used for serialization.
	// The protocol stack must match between client and server
	fProtocolFactory := frugal.NewFProtocolFactory(thrift.NewTBinaryProtocolFactoryDefault())

	// Create a handler. Each incoming request at the processor is sent to
	// the handler. Responses from the handler are returned back to the
	// client
	handler := &StoreHandler{}
	processor := music.NewFStoreProcessor(handler)

	// Start the server using the configured processor, and protocol
	http.HandleFunc("/frugal", frugal.NewFrugalHandlerFunc(processor, fProtocolFactory))
	func() {
		fmt.Println("Starting the http server...")
		http.ListenAndServe(":9090", http.DefaultServeMux)
	}()
}

// StoreHandler handles all incoming requests to the server.
// The handler must satisfy the interface the server exposes.
type StoreHandler struct{}

// BuyAlbum always buys the same album
func (f *StoreHandler) BuyAlbum(ctx *frugal.FContext, ASIN string, acct string) (r *music.Album, err error) {
	album := &music.Album{
		ASIN:     "c54d385a-5024-4f3f-86ef-6314546a7e7f",
		Duration: 1200,
		Tracks: []*music.Track{&music.Track{
			Title:     "Comme des enfants",
			Artist:    "Coeur de pirate",
			Publisher: "Grosse Boîte",
			Composer:  "Béatrice Martin",
			Duration:  169,
			Pro:       music.PerfRightsOrg_ASCAP,
		}},
	}

	return album, nil
}

// EnterAlbumGiveaway always returns true
func (f *StoreHandler) EnterAlbumGiveaway(ctx *frugal.FContext, email string, name string) (r bool, err error) {
	return true, nil
}
