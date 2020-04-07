from typing import overload, NewType, Optional, Tuple

from OCC.Core.BRepAlgo import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.GeomAbs import *
from OCC.Core.TopTools import *
from OCC.Core.BRepBuilderAPI import *
from OCC.Core.TopOpeBRepBuild import *
from OCC.Core.TopAbs import *
from OCC.Core.Adaptor3d import *
from OCC.Core.gp import *
from OCC.Core.Geom import *


class BRepAlgo_CheckStatus:
	BRepAlgo_OK: int = ...
	BRepAlgo_NOK: int = ...

class BRepAlgo:
	@staticmethod
	def ConcatenateWire(self, Wire: TopoDS_Wire, Option: GeomAbs_Shape, AngularTolerance: Optional[float]) -> TopoDS_Wire: ...
	@staticmethod
	def ConcatenateWireC0(self, Wire: TopoDS_Wire) -> TopoDS_Edge: ...
	@staticmethod
	def IsTopologicallyValid(self, S: TopoDS_Shape) -> bool: ...
	@staticmethod
	def IsValid(self, S: TopoDS_Shape) -> bool: ...
	@staticmethod
	def IsValid(self, theArgs: TopTools_ListOfShape, theResult: TopoDS_Shape, closedSolid: Optional[bool], GeomCtrl: Optional[bool]) -> bool: ...

class BRepAlgo_AsDes(Standard_Transient):
	def __init__(self) -> None: ...
	def Add(self, S: TopoDS_Shape, SS: TopoDS_Shape) -> None: ...
	def Add(self, S: TopoDS_Shape, SS: TopTools_ListOfShape) -> None: ...
	def Ascendant(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def ChangeDescendant(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def Clear(self) -> None: ...
	def Descendant(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def HasAscendant(self, S: TopoDS_Shape) -> bool: ...
	def HasCommonDescendant(self, S1: TopoDS_Shape, S2: TopoDS_Shape, LC: TopTools_ListOfShape) -> bool: ...
	def HasDescendant(self, S: TopoDS_Shape) -> bool: ...
	def Remove(self, S: TopoDS_Shape) -> None: ...
	def Replace(self, OldS: TopoDS_Shape, NewS: TopoDS_Shape) -> None: ...

class BRepAlgo_BooleanOperation(BRepBuilderAPI_MakeShape):
	def Builder(self) -> TopOpeBRepBuild_HBuilder: ...
	def IsDeleted(self, S: TopoDS_Shape) -> bool: ...
	def Modified(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def Perform(self, St1: TopAbs_State, St2: TopAbs_State) -> None: ...
	def PerformDS(self) -> None: ...
	def Shape1(self) -> TopoDS_Shape: ...
	def Shape2(self) -> TopoDS_Shape: ...

class BRepAlgo_FaceRestrictor:
	def __init__(self) -> None: ...
	def Add(self, W: TopoDS_Wire) -> None: ...
	def Clear(self) -> None: ...
	def Current(self) -> TopoDS_Face: ...
	def Init(self, F: TopoDS_Face, Proj: Optional[bool], ControlOrientation: Optional[bool]) -> None: ...
	def IsDone(self) -> bool: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Perform(self) -> None: ...

class BRepAlgo_Image:
	def __init__(self) -> None: ...
	def Add(self, OldS: TopoDS_Shape, NewS: TopoDS_Shape) -> None: ...
	def Add(self, OldS: TopoDS_Shape, NewS: TopTools_ListOfShape) -> None: ...
	def Bind(self, OldS: TopoDS_Shape, NewS: TopoDS_Shape) -> None: ...
	def Bind(self, OldS: TopoDS_Shape, NewS: TopTools_ListOfShape) -> None: ...
	def Clear(self) -> None: ...
	def Compact(self) -> None: ...
	def Filter(self, S: TopoDS_Shape, ShapeType: TopAbs_ShapeEnum) -> None: ...
	def HasImage(self, S: TopoDS_Shape) -> bool: ...
	def Image(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def ImageFrom(self, S: TopoDS_Shape) -> TopoDS_Shape: ...
	def IsImage(self, S: TopoDS_Shape) -> bool: ...
	def LastImage(self, S: TopoDS_Shape, L: TopTools_ListOfShape) -> None: ...
	def Remove(self, S: TopoDS_Shape) -> None: ...
	def Root(self, S: TopoDS_Shape) -> TopoDS_Shape: ...
	def Roots(self) -> TopTools_ListOfShape: ...
	def SetRoot(self, S: TopoDS_Shape) -> None: ...

class BRepAlgo_Loop:
	def __init__(self) -> None: ...
	def AddConstEdge(self, E: TopoDS_Edge) -> None: ...
	def AddConstEdges(self, LE: TopTools_ListOfShape) -> None: ...
	def AddEdge(self, E: TopoDS_Edge, LV: TopTools_ListOfShape) -> None: ...
	def CutEdge(self, E: TopoDS_Edge, VonE: TopTools_ListOfShape, NE: TopTools_ListOfShape) -> None: ...
	def GetVerticesForSubstitute(self, VerVerMap: TopTools_DataMapOfShapeShape) -> None: ...
	def Init(self, F: TopoDS_Face) -> None: ...
	def NewEdges(self, E: TopoDS_Edge) -> TopTools_ListOfShape: ...
	def NewFaces(self) -> TopTools_ListOfShape: ...
	def NewWires(self) -> TopTools_ListOfShape: ...
	def Perform(self) -> None: ...
	def VerticesForSubstitute(self, VerVerMap: TopTools_DataMapOfShapeShape) -> None: ...
	def WiresToFaces(self) -> None: ...

class BRepAlgo_NormalProjection:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def Add(self, ToProj: TopoDS_Shape) -> None: ...
	def Ancestor(self, E: TopoDS_Edge) -> TopoDS_Shape: ...
	def Build(self) -> None: ...
	def BuildWire(self, Liste: TopTools_ListOfShape) -> bool: ...
	def Compute3d(self, With3d: Optional[bool]) -> None: ...
	def Couple(self, E: TopoDS_Edge) -> TopoDS_Shape: ...
	def Generated(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def Init(self, S: TopoDS_Shape) -> None: ...
	def IsDone(self) -> bool: ...
	def IsElementary(self, C: Adaptor3d_Curve) -> bool: ...
	def Projection(self) -> TopoDS_Shape: ...
	def SetDefaultParams(self) -> None: ...
	def SetLimit(self, FaceBoundaries: Optional[bool]) -> None: ...
	def SetMaxDistance(self, MaxDist: float) -> None: ...
	def SetParams(self, Tol3D: float, Tol2D: float, InternalContinuity: GeomAbs_Shape, MaxDegree: int, MaxSeg: int) -> None: ...

class BRepAlgo_Tool:
	@staticmethod
	def Deboucle3D(self, S: TopoDS_Shape, Boundary: TopTools_MapOfShape) -> TopoDS_Shape: ...

class BRepAlgo_Common(BRepAlgo_BooleanOperation):
	def __init__(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...

class BRepAlgo_Cut(BRepAlgo_BooleanOperation):
	def __init__(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...

class BRepAlgo_Fuse(BRepAlgo_BooleanOperation):
	def __init__(self, S1: TopoDS_Shape, S2: TopoDS_Shape) -> None: ...

class BRepAlgo_Section(BRepAlgo_BooleanOperation):
	@overload
	def __init__(self, Sh1: TopoDS_Shape, Sh2: TopoDS_Shape, PerformNow: Optional[bool]) -> None: ...
	@overload
	def __init__(self, Sh: TopoDS_Shape, Pl: gp_Pln, PerformNow: Optional[bool]) -> None: ...
	@overload
	def __init__(self, Sh: TopoDS_Shape, Sf: Geom_Surface, PerformNow: Optional[bool]) -> None: ...
	@overload
	def __init__(self, Sf: Geom_Surface, Sh: TopoDS_Shape, PerformNow: Optional[bool]) -> None: ...
	@overload
	def __init__(self, Sf1: Geom_Surface, Sf2: Geom_Surface, PerformNow: Optional[bool]) -> None: ...
	def Approximation(self, B: bool) -> None: ...
	def Build(self) -> None: ...
	def ComputePCurveOn1(self, B: bool) -> None: ...
	def ComputePCurveOn2(self, B: bool) -> None: ...
	def HasAncestorFaceOn1(self, E: TopoDS_Shape, F: TopoDS_Shape) -> bool: ...
	def HasAncestorFaceOn2(self, E: TopoDS_Shape, F: TopoDS_Shape) -> bool: ...
	def Init1(self, S1: TopoDS_Shape) -> None: ...
	def Init1(self, Pl: gp_Pln) -> None: ...
	def Init1(self, Sf: Geom_Surface) -> None: ...
	def Init2(self, S2: TopoDS_Shape) -> None: ...
	def Init2(self, Pl: gp_Pln) -> None: ...
	def Init2(self, Sf: Geom_Surface) -> None: ...
