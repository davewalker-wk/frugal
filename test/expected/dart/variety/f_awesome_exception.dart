// Autogenerated by Frugal Compiler (2.22.1)
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING

import 'dart:typed_data' show Uint8List;
import 'package:thrift/thrift.dart' as thrift;
import 'package:variety/variety.dart' as t_variety;
import 'package:actual_base_dart/actual_base_dart.dart' as t_actual_base_dart;
import 'package:intermediate_include/intermediate_include.dart' as t_intermediate_include;
import 'package:validStructs/validStructs.dart' as t_validStructs;
import 'package:ValidTypes/ValidTypes.dart' as t_ValidTypes;
import 'package:subdir_include_ns/subdir_include_ns.dart' as t_subdir_include_ns;

class AwesomeException implements thrift.TBase, Exception {
  static final thrift.TStruct _STRUCT_DESC = new thrift.TStruct("AwesomeException");
  static final thrift.TField _ID_FIELD_DESC = new thrift.TField("ID", thrift.TType.I64, 1);
  static final thrift.TField _REASON_FIELD_DESC = new thrift.TField("Reason", thrift.TType.STRING, 2);
  static final thrift.TField _DEPR_FIELD_DESC = new thrift.TField("depr", thrift.TType.BOOL, 3);

  /// ID is a unique identifier for an awesome exception.
  int _iD = 0;
  static const int ID = 1;
  /// Reason contains the error message.
  String _reason;
  static const int REASON = 2;
  /// Deprecated: use something else
  @deprecated
  bool _depr = false;
  static const int DEPR = 3;

  bool __isset_iD = false;
  bool __isset_depr = false;

  AwesomeException() {
  }

  /// ID is a unique identifier for an awesome exception.
  int get iD => this._iD;

  /// ID is a unique identifier for an awesome exception.
  set iD(int iD) {
    this._iD = iD;
    this.__isset_iD = true;
  }

  bool isSetID() => this.__isset_iD;

  unsetID() {
    this.__isset_iD = false;
  }

  /// Reason contains the error message.
  String get reason => this._reason;

  /// Reason contains the error message.
  set reason(String reason) {
    this._reason = reason;
  }

  bool isSetReason() => this.reason != null;

  unsetReason() {
    this.reason = null;
  }

  /// Deprecated: use something else
  @deprecated
  bool get depr => this._depr;

  /// Deprecated: use something else
  @deprecated
  set depr(bool depr) {
    this._depr = depr;
    this.__isset_depr = true;
  }

  @deprecated  bool isSetDepr() => this.__isset_depr;

  unsetDepr() {
    this.__isset_depr = false;
  }

  getFieldValue(int fieldID) {
    switch (fieldID) {
      case ID:
        return this.iD;
      case REASON:
        return this.reason;
      case DEPR:
        return this.depr;
      default:
        throw new ArgumentError("Field $fieldID doesn't exist!");
    }
  }

  setFieldValue(int fieldID, Object value) {
    switch(fieldID) {
      case ID:
        if(value == null) {
          unsetID();
        } else {
          this.iD = value as int;
        }
        break;

      case REASON:
        if(value == null) {
          unsetReason();
        } else {
          this.reason = value as String;
        }
        break;

      case DEPR:
        if(value == null) {
          unsetDepr();
        } else {
          this.depr = value as bool;
        }
        break;

      default:
        throw new ArgumentError("Field $fieldID doesn't exist!");
    }
  }

  // Returns true if the field corresponding to fieldID is set (has been assigned a value) and false otherwise
  bool isSet(int fieldID) {
    switch(fieldID) {
      case ID:
        return isSetID();
      case REASON:
        return isSetReason();
      case DEPR:
        return isSetDepr();
      default:
        throw new ArgumentError("Field $fieldID doesn't exist!");
    }
  }

  read(thrift.TProtocol iprot) {
    thrift.TField field;
    iprot.readStructBegin();
    while(true) {
      field = iprot.readFieldBegin();
      if(field.type == thrift.TType.STOP) {
        break;
      }
      switch(field.id) {
        case ID:
          if(field.type == thrift.TType.I64) {
            iD = iprot.readI64();
            this.__isset_iD = true;
          } else {
            thrift.TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case REASON:
          if(field.type == thrift.TType.STRING) {
            reason = iprot.readString();
          } else {
            thrift.TProtocolUtil.skip(iprot, field.type);
          }
          break;
        case DEPR:
          if(field.type == thrift.TType.BOOL) {
            depr = iprot.readBool();
            this.__isset_depr = true;
          } else {
            thrift.TProtocolUtil.skip(iprot, field.type);
          }
          break;
        default:
          thrift.TProtocolUtil.skip(iprot, field.type);
          break;
      }
      iprot.readFieldEnd();
    }
    iprot.readStructEnd();

    // check for required fields of primitive type, which can't be checked in the validate method
    validate();
  }

  write(thrift.TProtocol oprot) {
    validate();

    oprot.writeStructBegin(_STRUCT_DESC);
    oprot.writeFieldBegin(_ID_FIELD_DESC);
    oprot.writeI64(iD);
    oprot.writeFieldEnd();
    if(this.reason != null) {
      oprot.writeFieldBegin(_REASON_FIELD_DESC);
      oprot.writeString(reason);
      oprot.writeFieldEnd();
    }
    oprot.writeFieldBegin(_DEPR_FIELD_DESC);
    oprot.writeBool(depr);
    oprot.writeFieldEnd();
    oprot.writeFieldStop();
    oprot.writeStructEnd();
  }

  String toString() {
    StringBuffer ret = new StringBuffer("AwesomeException(");

    ret.write("iD:");
    ret.write(this.iD);

    ret.write(", ");
    ret.write("reason:");
    if(this.reason == null) {
      ret.write("null");
    } else {
      ret.write(this.reason);
    }

    ret.write(", ");
    ret.write("depr:");
    ret.write(this.depr);

    ret.write(")");

    return ret.toString();
  }

  bool operator ==(Object o) {
    if(o == null || !(o is AwesomeException)) {
      return false;
    }
    AwesomeException other = o as AwesomeException;
    return this.iD == other.iD
      && this.reason == other.reason
      && this.depr == other.depr;
  }

  int get hashCode {
    var value = 17;
    value = (value * 31) ^ iD.hashCode;
    value = (value * 31) ^ reason.hashCode;
    value = (value * 31) ^ depr.hashCode;
    return value;
  }

  AwesomeException clone({
    int iD: null,
    String reason: null,
    bool depr: null,
  }) {
    return new AwesomeException()
      ..iD = iD ?? this.iD
      ..reason = reason ?? this.reason
      ..depr = depr ?? this.depr;
  }

  validate() {
    // check for required fields
    // check that fields of type enum have valid values
  }
}
