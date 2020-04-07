from typing import overload, NewType, Optional, Tuple

from OCC.Core.TDataXtd import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TDF import *
from OCC.Core.gp import *
from OCC.Core.TNaming import *
from OCC.Core.TDataStd import *
from OCC.Core.Quantity import *
from OCC.Core.TopoDS import *
from OCC.Core.Poly import *
from OCC.Core.TShort import *


class TDataXtd_ConstraintEnum:
	TDataXtd_RADIUS: int = ...
	TDataXtd_DIAMETER: int = ...
	TDataXtd_MINOR_RADIUS: int = ...
	TDataXtd_MAJOR_RADIUS: int = ...
	TDataXtd_TANGENT: int = ...
	TDataXtd_PARALLEL: int = ...
	TDataXtd_PERPENDICULAR: int = ...
	TDataXtd_CONCENTRIC: int = ...
	TDataXtd_COINCIDENT: int = ...
	TDataXtd_DISTANCE: int = ...
	TDataXtd_ANGLE: int = ...
	TDataXtd_EQUAL_RADIUS: int = ...
	TDataXtd_SYMMETRY: int = ...
	TDataXtd_MIDPOINT: int = ...
	TDataXtd_EQUAL_DISTANCE: int = ...
	TDataXtd_FIX: int = ...
	TDataXtd_RIGID: int = ...
	TDataXtd_FROM: int = ...
	TDataXtd_AXIS: int = ...
	TDataXtd_MATE: int = ...
	TDataXtd_ALIGN_FACES: int = ...
	TDataXtd_ALIGN_AXES: int = ...
	TDataXtd_AXES_ANGLE: int = ...
	TDataXtd_FACES_ANGLE: int = ...
	TDataXtd_ROUND: int = ...
	TDataXtd_OFFSET: int = ...

class TDataXtd_GeometryEnum:
	TDataXtd_ANY_GEOM: int = ...
	TDataXtd_POINT: int = ...
	TDataXtd_LINE: int = ...
	TDataXtd_CIRCLE: int = ...
	TDataXtd_ELLIPSE: int = ...
	TDataXtd_SPLINE: int = ...
	TDataXtd_PLANE: int = ...
	TDataXtd_CYLINDER: int = ...

class TDataXtd:
	@staticmethod
	def IDList(self, anIDList: TDF_IDList) -> None: ...

class TDataXtd_Axis(TDF_Attribute):
	def __init__(self) -> None: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def Restore(self, with_: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(self, label: TDF_Label) -> TDataXtd_Axis: ...
	@staticmethod
	def Set(self, label: TDF_Label, L: gp_Lin) -> TDataXtd_Axis: ...

class TDataXtd_Constraint(TDF_Attribute):
	def __init__(self) -> None: ...
	def ClearGeometries(self) -> None: ...
	@staticmethod
	def CollectChildConstraints(self, aLabel: TDF_Label, TheList: TDF_LabelList) -> None: ...
	def GetGeometry(self, Index: int) -> TNaming_NamedShape: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def GetPlane(self) -> TNaming_NamedShape: ...
	def GetType(self) -> TDataXtd_ConstraintEnum: ...
	def GetValue(self) -> TDataStd_Real: ...
	def ID(self) -> Standard_GUID: ...
	def Inverted(self, status: bool) -> None: ...
	def Inverted(self) -> bool: ...
	def IsDimension(self) -> bool: ...
	def IsPlanar(self) -> bool: ...
	def NbGeometries(self) -> int: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def References(self, DS: TDF_DataSet) -> None: ...
	def Restore(self, With: TDF_Attribute) -> None: ...
	def Reversed(self, status: bool) -> None: ...
	def Reversed(self) -> bool: ...
	@staticmethod
	def Set(self, label: TDF_Label) -> TDataXtd_Constraint: ...
	def Set(self, type: TDataXtd_ConstraintEnum, G1: TNaming_NamedShape) -> None: ...
	def Set(self, type: TDataXtd_ConstraintEnum, G1: TNaming_NamedShape, G2: TNaming_NamedShape) -> None: ...
	def Set(self, type: TDataXtd_ConstraintEnum, G1: TNaming_NamedShape, G2: TNaming_NamedShape, G3: TNaming_NamedShape) -> None: ...
	def Set(self, type: TDataXtd_ConstraintEnum, G1: TNaming_NamedShape, G2: TNaming_NamedShape, G3: TNaming_NamedShape, G4: TNaming_NamedShape) -> None: ...
	def SetGeometry(self, Index: int, G: TNaming_NamedShape) -> None: ...
	def SetPlane(self, plane: TNaming_NamedShape) -> None: ...
	def SetType(self, CTR: TDataXtd_ConstraintEnum) -> None: ...
	def SetValue(self, V: TDataStd_Real) -> None: ...
	def Verified(self) -> bool: ...
	def Verified(self, status: bool) -> None: ...

class TDataXtd_Geometry(TDF_Attribute):
	def __init__(self) -> None: ...
	@staticmethod
	def Axis(self, L: TDF_Label, G: gp_Ax1) -> bool: ...
	@staticmethod
	def Axis(self, S: TNaming_NamedShape, G: gp_Ax1) -> bool: ...
	@staticmethod
	def Circle(self, L: TDF_Label, G: gp_Circ) -> bool: ...
	@staticmethod
	def Circle(self, S: TNaming_NamedShape, G: gp_Circ) -> bool: ...
	@staticmethod
	def Cylinder(self, L: TDF_Label, G: gp_Cylinder) -> bool: ...
	@staticmethod
	def Cylinder(self, S: TNaming_NamedShape, G: gp_Cylinder) -> bool: ...
	@staticmethod
	def Ellipse(self, L: TDF_Label, G: gp_Elips) -> bool: ...
	@staticmethod
	def Ellipse(self, S: TNaming_NamedShape, G: gp_Elips) -> bool: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def GetType(self) -> TDataXtd_GeometryEnum: ...
	def ID(self) -> Standard_GUID: ...
	@staticmethod
	def Line(self, L: TDF_Label, G: gp_Lin) -> bool: ...
	@staticmethod
	def Line(self, S: TNaming_NamedShape, G: gp_Lin) -> bool: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	@staticmethod
	def Plane(self, L: TDF_Label, G: gp_Pln) -> bool: ...
	@staticmethod
	def Plane(self, S: TNaming_NamedShape, G: gp_Pln) -> bool: ...
	@staticmethod
	def Point(self, L: TDF_Label, G: gp_Pnt) -> bool: ...
	@staticmethod
	def Point(self, S: TNaming_NamedShape, G: gp_Pnt) -> bool: ...
	def Restore(self, with_: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(self, label: TDF_Label) -> TDataXtd_Geometry: ...
	def SetType(self, T: TDataXtd_GeometryEnum) -> None: ...
	@staticmethod
	def Type(self, L: TDF_Label) -> TDataXtd_GeometryEnum: ...
	@staticmethod
	def Type(self, S: TNaming_NamedShape) -> TDataXtd_GeometryEnum: ...

class TDataXtd_Pattern(TDF_Attribute):
	def ComputeTrsfs(self, Trsfs: TDataXtd_Array1OfTrsf) -> None: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	def NbTrsfs(self) -> int: ...
	def PatternID(self) -> Standard_GUID: ...

class TDataXtd_Placement(TDF_Attribute):
	def __init__(self) -> None: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def Restore(self, With: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(self, label: TDF_Label) -> TDataXtd_Placement: ...

class TDataXtd_Plane(TDF_Attribute):
	def __init__(self) -> None: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def Restore(self, With: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(self, label: TDF_Label) -> TDataXtd_Plane: ...
	@staticmethod
	def Set(self, label: TDF_Label, P: gp_Pln) -> TDataXtd_Plane: ...

class TDataXtd_Point(TDF_Attribute):
	def __init__(self) -> None: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def Restore(self, With: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(self, label: TDF_Label) -> TDataXtd_Point: ...
	@staticmethod
	def Set(self, label: TDF_Label, P: gp_Pnt) -> TDataXtd_Point: ...

class TDataXtd_Position(TDF_Attribute):
	def __init__(self) -> None: ...
	@staticmethod
	def Get(self, aLabel: TDF_Label, aPos: gp_Pnt) -> bool: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def GetPosition(self) -> gp_Pnt: ...
	def ID(self) -> Standard_GUID: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, intoAttribute: TDF_Attribute, aRelocTationable: TDF_RelocationTable) -> None: ...
	def Restore(self, anAttribute: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(self, aLabel: TDF_Label, aPos: gp_Pnt) -> None: ...
	@staticmethod
	def Set(self, aLabel: TDF_Label) -> TDataXtd_Position: ...
	def SetPosition(self, aPos: gp_Pnt) -> None: ...

class TDataXtd_Presentation(TDF_Attribute):
	def __init__(self) -> None: ...
	def AddSelectionMode(self, theSelectionMode: int, theTransaction: Optional[bool]) -> None: ...
	def BackupCopy(self) -> TDF_Attribute: ...
	def Color(self) -> Quantity_NameOfColor: ...
	def GetDriverGUID(self) -> Standard_GUID: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def GetNbSelectionModes(self) -> int: ...
	def HasOwnColor(self) -> bool: ...
	def HasOwnMaterial(self) -> bool: ...
	def HasOwnMode(self) -> bool: ...
	def HasOwnSelectionMode(self) -> bool: ...
	def HasOwnTransparency(self) -> bool: ...
	def HasOwnWidth(self) -> bool: ...
	def ID(self) -> Standard_GUID: ...
	def IsDisplayed(self) -> bool: ...
	def MaterialIndex(self) -> int: ...
	def Mode(self) -> int: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, intoAttribute: TDF_Attribute, aRelocTationable: TDF_RelocationTable) -> None: ...
	def Restore(self, anAttribute: TDF_Attribute) -> None: ...
	def SelectionMode(self, index: Optional[int]) -> int: ...
	@staticmethod
	def Set(self, theLabel: TDF_Label, theDriverId: Standard_GUID) -> TDataXtd_Presentation: ...
	def SetColor(self, theColor: Quantity_NameOfColor) -> None: ...
	def SetDisplayed(self, theIsDisplayed: bool) -> None: ...
	def SetDriverGUID(self, theGUID: Standard_GUID) -> None: ...
	def SetMaterialIndex(self, theMaterialIndex: int) -> None: ...
	def SetMode(self, theMode: int) -> None: ...
	def SetSelectionMode(self, theSelectionMode: int, theTransaction: Optional[bool]) -> None: ...
	def SetTransparency(self, theValue: float) -> None: ...
	def SetWidth(self, theWidth: float) -> None: ...
	def Transparency(self) -> float: ...
	@staticmethod
	def Unset(self, theLabel: TDF_Label) -> None: ...
	def UnsetColor(self) -> None: ...
	def UnsetMaterial(self) -> None: ...
	def UnsetMode(self) -> None: ...
	def UnsetSelectionMode(self) -> None: ...
	def UnsetTransparency(self) -> None: ...
	def UnsetWidth(self) -> None: ...
	def Width(self) -> float: ...

class TDataXtd_Shape(TDF_Attribute):
	def __init__(self) -> None: ...
	@staticmethod
	def Find(self, current: TDF_Label, S: TDataXtd_Shape) -> bool: ...
	@staticmethod
	def Get(self, label: TDF_Label) -> TopoDS_Shape: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def ID(self) -> Standard_GUID: ...
	@staticmethod
	def New(self, label: TDF_Label) -> TDataXtd_Shape: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def References(self, DS: TDF_DataSet) -> None: ...
	def Restore(self, with_: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(self, label: TDF_Label, shape: TopoDS_Shape) -> TDataXtd_Shape: ...

class TDataXtd_Triangulation(TDF_Attribute):
	def __init__(self) -> None: ...
	def Deflection(self) -> float: ...
	def Deflection(self, theDeflection: float) -> None: ...
	def Get(self) -> Poly_Triangulation: ...
	@staticmethod
	def GetID(self) -> Standard_GUID: ...
	def HasNormals(self) -> bool: ...
	def HasUVNodes(self) -> bool: ...
	def ID(self) -> Standard_GUID: ...
	def NbNodes(self) -> int: ...
	def NbTriangles(self) -> int: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Node(self, theIndex: int) -> gp_Pnt: ...
	def Normal(self, theIndex: int) -> gp_Dir: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def RemoveUVNodes(self) -> None: ...
	def Restore(self, theAttribute: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(self, theLabel: TDF_Label) -> TDataXtd_Triangulation: ...
	@staticmethod
	def Set(self, theLabel: TDF_Label, theTriangulation: Poly_Triangulation) -> TDataXtd_Triangulation: ...
	def Set(self, theTriangulation: Poly_Triangulation) -> None: ...
	def SetNode(self, theIndex: int, theNode: gp_Pnt) -> None: ...
	def SetNormal(self, theIndex: int, theNormal: gp_Dir) -> None: ...
	def SetNormals(self, theNormals: TShort_HArray1OfShortReal) -> None: ...
	def SetTriangle(self, theIndex: int, theTriangle: Poly_Triangle) -> None: ...
	def SetUVNode(self, theIndex: int, theUVNode: gp_Pnt2d) -> None: ...
	def Triangle(self, theIndex: int) -> Poly_Triangle: ...
	def UVNode(self, theIndex: int) -> gp_Pnt2d: ...

class TDataXtd_PatternStd(TDataXtd_Pattern):
	def __init__(self) -> None: ...
	def Axis1(self, Axis1: TNaming_NamedShape) -> None: ...
	def Axis1(self) -> TNaming_NamedShape: ...
	def Axis1Reversed(self, Axis1Reversed: bool) -> None: ...
	def Axis1Reversed(self) -> bool: ...
	def Axis2(self, Axis2: TNaming_NamedShape) -> None: ...
	def Axis2(self) -> TNaming_NamedShape: ...
	def Axis2Reversed(self, Axis2Reversed: bool) -> None: ...
	def Axis2Reversed(self) -> bool: ...
	def ComputeTrsfs(self, Trsfs: TDataXtd_Array1OfTrsf) -> None: ...
	@staticmethod
	def GetPatternID(self) -> Standard_GUID: ...
	def Mirror(self, plane: TNaming_NamedShape) -> None: ...
	def Mirror(self) -> TNaming_NamedShape: ...
	def NbInstances1(self, NbInstances1: TDataStd_Integer) -> None: ...
	def NbInstances1(self) -> TDataStd_Integer: ...
	def NbInstances2(self, NbInstances2: TDataStd_Integer) -> None: ...
	def NbInstances2(self) -> TDataStd_Integer: ...
	def NbTrsfs(self) -> int: ...
	def NewEmpty(self) -> TDF_Attribute: ...
	def Paste(self, Into: TDF_Attribute, RT: TDF_RelocationTable) -> None: ...
	def PatternID(self) -> Standard_GUID: ...
	def References(self, aDataSet: TDF_DataSet) -> None: ...
	def Restore(self, With: TDF_Attribute) -> None: ...
	@staticmethod
	def Set(self, label: TDF_Label) -> TDataXtd_PatternStd: ...
	def Signature(self, signature: int) -> None: ...
	def Signature(self) -> int: ...
	def Value1(self, value: TDataStd_Real) -> None: ...
	def Value1(self) -> TDataStd_Real: ...
	def Value2(self, value: TDataStd_Real) -> None: ...
	def Value2(self) -> TDataStd_Real: ...
