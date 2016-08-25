#
# Autogenerated by Frugal Compiler (1.15.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import actual_base.python.ttypes

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol


class HealthCondition:
    PASS = 1
    WARN = 2
    FAIL = 3
    UNKNOWN = 4

    _VALUES_TO_NAMES = {
        1: "PASS",
        2: "WARN",
        3: "FAIL",
        4: "UNKNOWN",
    }

    _NAMES_TO_VALUES = {
        "PASS": 1,
        "WARN": 2,
        "FAIL": 3,
        "UNKNOWN": 4,
    }

class ItsAnEnum:
    FIRST = 2
    SECOND = 3
    THIRD = 4
    fourth = 5
    Fifth = 6
    sIxItH = 7

    _VALUES_TO_NAMES = {
        2: "FIRST",
        3: "SECOND",
        4: "THIRD",
        5: "fourth",
        6: "Fifth",
        7: "sIxItH",
    }

    _NAMES_TO_VALUES = {
        "FIRST": 2,
        "SECOND": 3,
        "THIRD": 4,
        "fourth": 5,
        "Fifth": 6,
        "sIxItH": 7,
    }

class TestBase:
    """
    Attributes:
     - base_struct
    """
    def __init__(self, base_struct=None):
        self.base_struct = base_struct

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.base_struct = actual_base.python.ttypes.thing()
                    self.base_struct.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('TestBase')
        if self.base_struct is not None:
            oprot.writeFieldBegin('base_struct', TType.STRUCT, 1)
            self.base_struct.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.base_struct)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class Event:
    """
    This docstring gets added to the generated code because it has
    the @ sign.
    
    Attributes:
     - ID: ID is a unique identifier for an event.
     - Message: Message contains the event payload.
    """
    _DEFAULT_ID_MARKER = -1
    def __init__(self, ID=_DEFAULT_ID_MARKER, Message=None):
        self.ID = ID
        self.Message = Message

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.ID = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.Message = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('Event')
        if self.ID is not None:
            oprot.writeFieldBegin('ID', TType.I64, 1)
            oprot.writeI64(self.ID)
            oprot.writeFieldEnd()
        if self.Message is not None:
            oprot.writeFieldBegin('Message', TType.STRING, 2)
            oprot.writeString(self.Message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.ID)
        value = (value * 31) ^ hash(self.Message)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class TestingDefaults:
    """
    Attributes:
     - ID2
     - ev1
     - ev2
     - ID
     - thing
     - thing2
     - listfield
     - ID3
     - bin_field
     - bin_field2
     - bin_field3
     - bin_field4
     - list2
     - list3
     - list4
     - a_map
     - status
     - base_status
    """
    _DEFAULT_ID2_MARKER = -1
    _DEFAULT_ev1_MARKER = object()
    _DEFAULT_ev2_MARKER = object()
    _DEFAULT_ID_MARKER = -2
    _DEFAULT_thing_MARKER = "a constant"
    _DEFAULT_thing2_MARKER = "another constant"
    _DEFAULT_listfield_MARKER = object()
    _DEFAULT_ID3_MARKER = -1
    _DEFAULT_bin_field4_MARKER = "hello"
    _DEFAULT_list2_MARKER = object()
    _DEFAULT_list4_MARKER = object()
    _DEFAULT_a_map_MARKER = object()
    _DEFAULT_status_MARKER = 1
    _DEFAULT_base_status_MARKER = 3
    def __init__(self, ID2=_DEFAULT_ID2_MARKER, ev1=_DEFAULT_ev1_MARKER, ev2=_DEFAULT_ev2_MARKER, ID=_DEFAULT_ID_MARKER, thing=_DEFAULT_thing_MARKER, thing2=_DEFAULT_thing2_MARKER, listfield=_DEFAULT_listfield_MARKER, ID3=_DEFAULT_ID3_MARKER, bin_field=None, bin_field2=None, bin_field3=None, bin_field4=_DEFAULT_bin_field4_MARKER, list2=_DEFAULT_list2_MARKER, list3=None, list4=_DEFAULT_list4_MARKER, a_map=_DEFAULT_a_map_MARKER, status=_DEFAULT_status_MARKER, base_status=_DEFAULT_base_status_MARKER):
        self.ID2 = ID2
        if ev1 is self._DEFAULT_ev1_MARKER:
            ev1 = Event(**{
                "ID": -1,
                "Message": "a message",
            })
        self.ev1 = ev1
        if ev2 is self._DEFAULT_ev2_MARKER:
            ev2 = Event(**{
                "ID": 5,
                "Message": "a message2",
            })
        self.ev2 = ev2
        self.ID = ID
        self.thing = thing
        self.thing2 = thing2
        if listfield is self._DEFAULT_listfield_MARKER:
            listfield = [
                1,
                2,
                3,
                4,
                5,
            ]
        self.listfield = listfield
        self.ID3 = ID3
        self.bin_field = bin_field
        self.bin_field2 = bin_field2
        self.bin_field3 = bin_field3
        self.bin_field4 = bin_field4
        if list2 is self._DEFAULT_list2_MARKER:
            list2 = [
                1,
                3,
                4,
                5,
                8,
            ]
        self.list2 = list2
        self.list3 = list3
        if list4 is self._DEFAULT_list4_MARKER:
            list4 = [
                1,
                2,
                3,
                6,
            ]
        self.list4 = list4
        if a_map is self._DEFAULT_a_map_MARKER:
            a_map = {
                "k1": "v1",
                "k2": "v2",
            }
        self.a_map = a_map
        self.status = status
        self.base_status = base_status

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.ID2 = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.ev1 = Event()
                    self.ev1.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.ev2 = Event()
                    self.ev2.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.ID = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.thing = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.thing2 = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.listfield = []
                    (_, _elem0) = iprot.readListBegin()
                    for _ in range(_elem0):
                        _elem1 = iprot.readI32()
                        self.listfield.append(_elem1)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I64:
                    self.ID3 = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.bin_field = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.bin_field2 = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.bin_field3 = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.bin_field4 = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.LIST:
                    self.list2 = []
                    (_, _elem2) = iprot.readListBegin()
                    for _ in range(_elem2):
                        _elem3 = iprot.readI32()
                        self.list2.append(_elem3)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.LIST:
                    self.list3 = []
                    (_, _elem4) = iprot.readListBegin()
                    for _ in range(_elem4):
                        _elem5 = iprot.readI32()
                        self.list3.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.LIST:
                    self.list4 = []
                    (_, _elem6) = iprot.readListBegin()
                    for _ in range(_elem6):
                        _elem7 = iprot.readI32()
                        self.list4.append(_elem7)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.MAP:
                    self.a_map = {}
                    (_, _, _elem8) = iprot.readMapBegin()
                    for _ in range(_elem8):
                        _elem10 = iprot.readString()
                        _elem9 = iprot.readString()
                        self.a_map[_elem10] = _elem9
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.I32:
                    self.base_status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('TestingDefaults')
        if self.ID2 is not None:
            oprot.writeFieldBegin('ID2', TType.I64, 1)
            oprot.writeI64(self.ID2)
            oprot.writeFieldEnd()
        if self.ev1 is not None:
            oprot.writeFieldBegin('ev1', TType.STRUCT, 2)
            self.ev1.write(oprot)
            oprot.writeFieldEnd()
        if self.ev2 is not None:
            oprot.writeFieldBegin('ev2', TType.STRUCT, 3)
            self.ev2.write(oprot)
            oprot.writeFieldEnd()
        if self.ID is not None:
            oprot.writeFieldBegin('ID', TType.I64, 4)
            oprot.writeI64(self.ID)
            oprot.writeFieldEnd()
        if self.thing is not None:
            oprot.writeFieldBegin('thing', TType.STRING, 5)
            oprot.writeString(self.thing)
            oprot.writeFieldEnd()
        if self.thing2 is not None:
            oprot.writeFieldBegin('thing2', TType.STRING, 6)
            oprot.writeString(self.thing2)
            oprot.writeFieldEnd()
        if self.listfield is not None:
            oprot.writeFieldBegin('listfield', TType.LIST, 7)
            oprot.writeListBegin(TType.I32, len(self.listfield))
            for _elem11 in self.listfield:
                oprot.writeI32(_elem11)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.ID3 is not None:
            oprot.writeFieldBegin('ID3', TType.I64, 8)
            oprot.writeI64(self.ID3)
            oprot.writeFieldEnd()
        if self.bin_field is not None:
            oprot.writeFieldBegin('bin_field', TType.STRING, 9)
            oprot.writeString(self.bin_field)
            oprot.writeFieldEnd()
        if self.bin_field2 is not None:
            oprot.writeFieldBegin('bin_field2', TType.STRING, 10)
            oprot.writeString(self.bin_field2)
            oprot.writeFieldEnd()
        if self.bin_field3 is not None:
            oprot.writeFieldBegin('bin_field3', TType.STRING, 11)
            oprot.writeString(self.bin_field3)
            oprot.writeFieldEnd()
        if self.bin_field4 is not None:
            oprot.writeFieldBegin('bin_field4', TType.STRING, 12)
            oprot.writeString(self.bin_field4)
            oprot.writeFieldEnd()
        if self.list2 is not None:
            oprot.writeFieldBegin('list2', TType.LIST, 13)
            oprot.writeListBegin(TType.I32, len(self.list2))
            for _elem12 in self.list2:
                oprot.writeI32(_elem12)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.list3 is not None:
            oprot.writeFieldBegin('list3', TType.LIST, 14)
            oprot.writeListBegin(TType.I32, len(self.list3))
            for _elem13 in self.list3:
                oprot.writeI32(_elem13)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.list4 is not None:
            oprot.writeFieldBegin('list4', TType.LIST, 15)
            oprot.writeListBegin(TType.I32, len(self.list4))
            for _elem14 in self.list4:
                oprot.writeI32(_elem14)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.a_map is not None:
            oprot.writeFieldBegin('a_map', TType.MAP, 16)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.a_map))
            for _elem16, _elem15 in self.a_map.items():
                oprot.writeString(_elem16)
                oprot.writeString(_elem15)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 17)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.base_status is not None:
            oprot.writeFieldBegin('base_status', TType.I32, 18)
            oprot.writeI32(self.base_status)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.status is None:
            raise TProtocol.TProtocolException(message='Required field status is unset!')
        if self.base_status is None:
            raise TProtocol.TProtocolException(message='Required field base_status is unset!')
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.ID2)
        value = (value * 31) ^ hash(self.ev1)
        value = (value * 31) ^ hash(self.ev2)
        value = (value * 31) ^ hash(self.ID)
        value = (value * 31) ^ hash(self.thing)
        value = (value * 31) ^ hash(self.thing2)
        value = (value * 31) ^ hash(self.listfield)
        value = (value * 31) ^ hash(self.ID3)
        value = (value * 31) ^ hash(self.bin_field)
        value = (value * 31) ^ hash(self.bin_field2)
        value = (value * 31) ^ hash(self.bin_field3)
        value = (value * 31) ^ hash(self.bin_field4)
        value = (value * 31) ^ hash(self.list2)
        value = (value * 31) ^ hash(self.list3)
        value = (value * 31) ^ hash(self.list4)
        value = (value * 31) ^ hash(self.a_map)
        value = (value * 31) ^ hash(self.status)
        value = (value * 31) ^ hash(self.base_status)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class EventWrapper:
    """
    Attributes:
     - ID
     - Ev
     - Events
     - Events2
     - EventMap
     - Nums
     - Enums
     - aBoolField
     - a_union
     - typedefOfTypedef
    """
    def __init__(self, ID=None, Ev=None, Events=None, Events2=None, EventMap=None, Nums=None, Enums=None, aBoolField=None, a_union=None, typedefOfTypedef=None):
        self.ID = ID
        self.Ev = Ev
        self.Events = Events
        self.Events2 = Events2
        self.EventMap = EventMap
        self.Nums = Nums
        self.Enums = Enums
        self.aBoolField = aBoolField
        self.a_union = a_union
        self.typedefOfTypedef = typedefOfTypedef

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.ID = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.Ev = Event()
                    self.Ev.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.Events = []
                    (_, _elem17) = iprot.readListBegin()
                    for _ in range(_elem17):
                        _elem18 = Event()
                        _elem18.read(iprot)
                        self.Events.append(_elem18)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.SET:
                    self.Events2 = set()
                    (_, _elem19) = iprot.readSetBegin()
                    for _ in range(_elem19):
                        _elem20 = Event()
                        _elem20.read(iprot)
                        self.Events2.add(_elem20)
                    iprot.readSetEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.MAP:
                    self.EventMap = {}
                    (_, _, _elem21) = iprot.readMapBegin()
                    for _ in range(_elem21):
                        _elem23 = iprot.readI64()
                        _elem22 = Event()
                        _elem22.read(iprot)
                        self.EventMap[_elem23] = _elem22
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.Nums = []
                    (_, _elem24) = iprot.readListBegin()
                    for _ in range(_elem24):
                        _elem25 = []
                        (_, _elem26) = iprot.readListBegin()
                        for _ in range(_elem26):
                            _elem27 = iprot.readI32()
                            _elem25.append(_elem27)
                        iprot.readListEnd()
                        self.Nums.append(_elem25)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.Enums = []
                    (_, _elem28) = iprot.readListBegin()
                    for _ in range(_elem28):
                        _elem29 = iprot.readI32()
                        self.Enums.append(_elem29)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.BOOL:
                    self.aBoolField = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRUCT:
                    self.a_union = TestingUnions()
                    self.a_union.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.typedefOfTypedef = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('EventWrapper')
        if self.ID is not None:
            oprot.writeFieldBegin('ID', TType.I64, 1)
            oprot.writeI64(self.ID)
            oprot.writeFieldEnd()
        if self.Ev is not None:
            oprot.writeFieldBegin('Ev', TType.STRUCT, 2)
            self.Ev.write(oprot)
            oprot.writeFieldEnd()
        if self.Events is not None:
            oprot.writeFieldBegin('Events', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.Events))
            for _elem30 in self.Events:
                _elem30.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.Events2 is not None:
            oprot.writeFieldBegin('Events2', TType.SET, 4)
            oprot.writeSetBegin(TType.STRUCT, len(self.Events2))
            for _elem31 in self.Events2:
                _elem31.write(oprot)
            oprot.writeSetEnd()
            oprot.writeFieldEnd()
        if self.EventMap is not None:
            oprot.writeFieldBegin('EventMap', TType.MAP, 5)
            oprot.writeMapBegin(TType.I64, TType.STRUCT, len(self.EventMap))
            for _elem33, _elem32 in self.EventMap.items():
                oprot.writeI64(_elem33)
                _elem32.write(oprot)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.Nums is not None:
            oprot.writeFieldBegin('Nums', TType.LIST, 6)
            oprot.writeListBegin(TType.LIST, len(self.Nums))
            for _elem34 in self.Nums:
                oprot.writeListBegin(TType.I32, len(_elem34))
                for _elem35 in _elem34:
                    oprot.writeI32(_elem35)
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.Enums is not None:
            oprot.writeFieldBegin('Enums', TType.LIST, 7)
            oprot.writeListBegin(TType.I32, len(self.Enums))
            for _elem36 in self.Enums:
                oprot.writeI32(_elem36)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.aBoolField is not None:
            oprot.writeFieldBegin('aBoolField', TType.BOOL, 8)
            oprot.writeBool(self.aBoolField)
            oprot.writeFieldEnd()
        if self.a_union is not None:
            oprot.writeFieldBegin('a_union', TType.STRUCT, 9)
            self.a_union.write(oprot)
            oprot.writeFieldEnd()
        if self.typedefOfTypedef is not None:
            oprot.writeFieldBegin('typedefOfTypedef', TType.STRING, 10)
            oprot.writeString(self.typedefOfTypedef)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.Ev is None:
            raise TProtocol.TProtocolException(message='Required field Ev is unset!')
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.ID)
        value = (value * 31) ^ hash(self.Ev)
        value = (value * 31) ^ hash(self.Events)
        value = (value * 31) ^ hash(self.Events2)
        value = (value * 31) ^ hash(self.EventMap)
        value = (value * 31) ^ hash(self.Nums)
        value = (value * 31) ^ hash(self.Enums)
        value = (value * 31) ^ hash(self.aBoolField)
        value = (value * 31) ^ hash(self.a_union)
        value = (value * 31) ^ hash(self.typedefOfTypedef)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class TestingUnions:
    """
    Attributes:
     - AnID
     - aString
     - someotherthing
     - AnInt16
     - Requests
    """
    def __init__(self, AnID=None, aString=None, someotherthing=None, AnInt16=None, Requests=None):
        self.AnID = AnID
        self.aString = aString
        self.someotherthing = someotherthing
        self.AnInt16 = AnInt16
        self.Requests = Requests

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.AnID = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.aString = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.someotherthing = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.AnInt16 = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.MAP:
                    self.Requests = {}
                    (_, _, _elem37) = iprot.readMapBegin()
                    for _ in range(_elem37):
                        _elem39 = iprot.readI32()
                        _elem38 = iprot.readString()
                        self.Requests[_elem39] = _elem38
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('TestingUnions')
        if self.AnID is not None:
            oprot.writeFieldBegin('AnID', TType.I64, 1)
            oprot.writeI64(self.AnID)
            oprot.writeFieldEnd()
        if self.aString is not None:
            oprot.writeFieldBegin('aString', TType.STRING, 2)
            oprot.writeString(self.aString)
            oprot.writeFieldEnd()
        if self.someotherthing is not None:
            oprot.writeFieldBegin('someotherthing', TType.I32, 3)
            oprot.writeI32(self.someotherthing)
            oprot.writeFieldEnd()
        if self.AnInt16 is not None:
            oprot.writeFieldBegin('AnInt16', TType.I16, 4)
            oprot.writeI16(self.AnInt16)
            oprot.writeFieldEnd()
        if self.Requests is not None:
            oprot.writeFieldBegin('Requests', TType.MAP, 5)
            oprot.writeMapBegin(TType.I32, TType.STRING, len(self.Requests))
            for _elem41, _elem40 in self.Requests.items():
                oprot.writeI32(_elem41)
                oprot.writeString(_elem40)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.AnID)
        value = (value * 31) ^ hash(self.aString)
        value = (value * 31) ^ hash(self.someotherthing)
        value = (value * 31) ^ hash(self.AnInt16)
        value = (value * 31) ^ hash(self.Requests)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class AwesomeException(TException):
    """
    Attributes:
     - ID: ID is a unique identifier for an awesome exception.
     - Reason: Reason contains the error message.
    """
    def __init__(self, ID=None, Reason=None):
        self.ID = ID
        self.Reason = Reason

    def read(self, iprot):
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.ID = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.Reason = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        oprot.writeStructBegin('AwesomeException')
        if self.ID is not None:
            oprot.writeFieldBegin('ID', TType.I64, 1)
            oprot.writeI64(self.ID)
            oprot.writeFieldEnd()
        if self.Reason is not None:
            oprot.writeFieldBegin('Reason', TType.STRING, 2)
            oprot.writeString(self.Reason)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __hash__(self):
        value = 17
        value = (value * 31) ^ hash(self.ID)
        value = (value * 31) ^ hash(self.Reason)
        return value

    def __repr__(self):
        L = ['%s=%r' % (key, value)
            for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

