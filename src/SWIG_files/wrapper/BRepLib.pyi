from typing import overload, NewType, Optional, Tuple

from OCC.Core.BRepLib import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *
from OCC.Core.TopoDS import *
from OCC.Core.GeomAbs import *
from OCC.Core.Geom2d import *
from OCC.Core.TopTools import *
from OCC.Core.Adaptor3d import *
from OCC.Core.Geom import *
from OCC.Core.BRepTools import *
from OCC.Core.TopLoc import *


class BRepLib_EdgeError:
	BRepLib_EdgeDone: int = ...
	BRepLib_PointProjectionFailed: int = ...
	BRepLib_ParameterOutOfRange: int = ...
	BRepLib_DifferentPointsOnClosedCurve: int = ...
	BRepLib_PointWithInfiniteParameter: int = ...
	BRepLib_DifferentsPointAndParameter: int = ...
	BRepLib_LineThroughIdenticPoints: int = ...

class BRepLib_ShellError:
	BRepLib_ShellDone: int = ...
	BRepLib_EmptyShell: int = ...
	BRepLib_DisconnectedShell: int = ...
	BRepLib_ShellParametersOutOfRange: int = ...

class BRepLib_ShapeModification:
	BRepLib_Preserved: int = ...
	BRepLib_Deleted: int = ...
	BRepLib_Trimmed: int = ...
	BRepLib_Merged: int = ...
	BRepLib_BoundaryModified: int = ...

class BRepLib_WireError:
	BRepLib_WireDone: int = ...
	BRepLib_EmptyWire: int = ...
	BRepLib_DisconnectedWire: int = ...
	BRepLib_NonManifoldWire: int = ...

class BRepLib_FaceError:
	BRepLib_FaceDone: int = ...
	BRepLib_NoFace: int = ...
	BRepLib_NotPlanar: int = ...
	BRepLib_CurveProjectionFailed: int = ...
	BRepLib_ParametersOutOfRange: int = ...

class BRepLib:
	@staticmethod
	def BuildCurve3d(self, E: TopoDS_Edge, Tolerance: Optional[float], Continuity: Optional[GeomAbs_Shape], MaxDegree: Optional[int], MaxSegment: Optional[int]) -> bool: ...
	@staticmethod
	def BuildCurves3d(self, S: TopoDS_Shape, Tolerance: float, Continuity: Optional[GeomAbs_Shape], MaxDegree: Optional[int], MaxSegment: Optional[int]) -> bool: ...
	@staticmethod
	def BuildCurves3d(self, S: TopoDS_Shape) -> bool: ...
	@staticmethod
	def BuildPCurveForEdgeOnPlane(self, theE: TopoDS_Edge, theF: TopoDS_Face) -> None: ...
	@staticmethod
	def BuildPCurveForEdgeOnPlane(self, theE: TopoDS_Edge, theF: TopoDS_Face, aC2D: Geom2d_Curve) -> bool: ...
	@staticmethod
	def CheckSameRange(self, E: TopoDS_Edge, Confusion: Optional[float]) -> bool: ...
	@staticmethod
	def EncodeRegularity(self, S: TopoDS_Shape, TolAng: Optional[float]) -> None: ...
	@staticmethod
	def EncodeRegularity(self, S: TopoDS_Shape, LE: TopTools_ListOfShape, TolAng: Optional[float]) -> None: ...
	@staticmethod
	def EncodeRegularity(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face, TolAng: Optional[float]) -> None: ...
	@staticmethod
	def EnsureNormalConsistency(self, S: TopoDS_Shape, theAngTol: Optional[float], ForceComputeNormals: Optional[bool]) -> bool: ...
	@staticmethod
	def ExtendFace(self, theF: TopoDS_Face, theExtVal: float, theExtUMin: bool, theExtUMax: bool, theExtVMin: bool, theExtVMax: bool, theFExtended: TopoDS_Face) -> None: ...
	@staticmethod
	def FindValidRange(self, theCurve: Adaptor3d_Curve, theTolE: float, theParV1: float, thePntV1: gp_Pnt, theTolV1: float, theParV2: float, thePntV2: gp_Pnt, theTolV2: float) -> Tuple[bool, float, float]: ...
	@staticmethod
	def FindValidRange(self, theEdge: TopoDS_Edge) -> Tuple[bool, float, float]: ...
	@staticmethod
	def OrientClosedSolid(self, solid: TopoDS_Solid) -> bool: ...
	@staticmethod
	def Plane(self, P: Geom_Plane) -> None: ...
	@staticmethod
	def Plane(self) -> Geom_Plane: ...
	@staticmethod
	def Precision(self, P: float) -> None: ...
	@staticmethod
	def Precision(self) -> float: ...
	@staticmethod
	def ReverseSortFaces(self, S: TopoDS_Shape, LF: TopTools_ListOfShape) -> None: ...
	@staticmethod
	def SameParameter(self, theEdge: TopoDS_Edge, Tolerance: Optional[float]) -> None: ...
	@staticmethod
	def SameParameter(self, theEdge: TopoDS_Edge, theTolerance: float, IsUseOldEdge: bool) -> Tuple[TopoDS_Edge, float]: ...
	@staticmethod
	def SameParameter(self, S: TopoDS_Shape, Tolerance: Optional[float], forced: Optional[bool]) -> None: ...
	@staticmethod
	def SameParameter(self, S: TopoDS_Shape, theReshaper: BRepTools_ReShape, Tolerance: Optional[float], forced: Optional[bool]) -> None: ...
	@staticmethod
	def SameRange(self, E: TopoDS_Edge, Tolerance: Optional[float]) -> None: ...
	@staticmethod
	def SortFaces(self, S: TopoDS_Shape, LF: TopTools_ListOfShape) -> None: ...
	@staticmethod
	def UpdateEdgeTol(self, E: TopoDS_Edge, MinToleranceRequest: float, MaxToleranceToCheck: float) -> bool: ...
	@staticmethod
	def UpdateEdgeTolerance(self, S: TopoDS_Shape, MinToleranceRequest: float, MaxToleranceToCheck: float) -> bool: ...
	@staticmethod
	def UpdateInnerTolerances(self, S: TopoDS_Shape) -> None: ...
	@staticmethod
	def UpdateTolerances(self, S: TopoDS_Shape, verifyFaceTolerance: Optional[bool]) -> None: ...
	@staticmethod
	def UpdateTolerances(self, S: TopoDS_Shape, theReshaper: BRepTools_ReShape, verifyFaceTolerance: Optional[bool]) -> None: ...

class BRepLib_CheckCurveOnSurface:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theEdge: TopoDS_Edge, theFace: TopoDS_Face) -> None: ...
	def Curve(self) -> Geom_Curve: ...
	def ErrorStatus(self) -> int: ...
	def Init(self, theEdge: TopoDS_Edge, theFace: TopoDS_Face) -> None: ...
	def IsDone(self) -> bool: ...
	def MaxDistance(self) -> float: ...
	def MaxParameter(self) -> float: ...
	def PCurve(self) -> Geom2d_Curve: ...
	def PCurve2(self) -> Geom2d_Curve: ...
	def Perform(self, isTheMultyTheradDisabled: Optional[bool]) -> None: ...
	def Range(self) -> Tuple[float, float]: ...
	def Surface(self) -> Geom_Surface: ...

class BRepLib_Command:
	def Check(self) -> None: ...
	def IsDone(self) -> bool: ...

class BRepLib_FindSurface:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shape, Tol: Optional[float], OnlyPlane: Optional[bool], OnlyClosed: Optional[bool]) -> None: ...
	def Existed(self) -> bool: ...
	def Found(self) -> bool: ...
	def Init(self, S: TopoDS_Shape, Tol: Optional[float], OnlyPlane: Optional[bool], OnlyClosed: Optional[bool]) -> None: ...
	def Location(self) -> TopLoc_Location: ...
	def Surface(self) -> Geom_Surface: ...
	def Tolerance(self) -> float: ...
	def ToleranceReached(self) -> float: ...

class BRepLib_FuseEdges:
	def __init__(self, theShape: TopoDS_Shape, PerformNow: Optional[bool]) -> None: ...
	def AvoidEdges(self, theMapEdg: TopTools_IndexedMapOfShape) -> None: ...
	def Edges(self, theMapLstEdg: TopTools_DataMapOfIntegerListOfShape) -> None: ...
	def Faces(self, theMapFac: TopTools_DataMapOfShapeShape) -> None: ...
	def NbVertices(self) -> int: ...
	def Perform(self) -> None: ...
	def ResultEdges(self, theMapEdg: TopTools_DataMapOfIntegerShape) -> None: ...
	def SetConcatBSpl(self, theConcatBSpl: Optional[bool]) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...

class BRepLib_MakeShape(BRepLib_Command):
	def Build(self) -> None: ...
	def DescendantFaces(self, F: TopoDS_Face) -> TopTools_ListOfShape: ...
	def FaceStatus(self, F: TopoDS_Face) -> BRepLib_ShapeModification: ...
	def FacesFromEdges(self, E: TopoDS_Edge) -> TopTools_ListOfShape: ...
	def HasDescendants(self, F: TopoDS_Face) -> bool: ...
	def NbSurfaces(self) -> int: ...
	def NewFaces(self, I: int) -> TopTools_ListOfShape: ...
	def Shape(self) -> TopoDS_Shape: ...

class BRepLib_MakeEdge(BRepLib_MakeShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
	@overload
	def __init__(self, L: gp_Lin) -> None: ...
	@overload
	def __init__(self, L: gp_Lin, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: gp_Lin, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
	@overload
	def __init__(self, L: gp_Lin, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, L: gp_Circ) -> None: ...
	@overload
	def __init__(self, L: gp_Circ, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: gp_Circ, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
	@overload
	def __init__(self, L: gp_Circ, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, L: gp_Elips) -> None: ...
	@overload
	def __init__(self, L: gp_Elips, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: gp_Elips, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
	@overload
	def __init__(self, L: gp_Elips, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, L: gp_Hypr) -> None: ...
	@overload
	def __init__(self, L: gp_Hypr, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: gp_Hypr, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
	@overload
	def __init__(self, L: gp_Hypr, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, L: gp_Parab) -> None: ...
	@overload
	def __init__(self, L: gp_Parab, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: gp_Parab, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
	@overload
	def __init__(self, L: gp_Parab, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, L: Geom_Curve) -> None: ...
	@overload
	def __init__(self, L: Geom_Curve, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: Geom_Curve, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
	@overload
	def __init__(self, L: Geom_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, L: Geom_Curve, P1: gp_Pnt, P2: gp_Pnt, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: Geom_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: Geom2d_Curve, S: Geom_Surface) -> None: ...
	@overload
	def __init__(self, L: Geom2d_Curve, S: Geom_Surface, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: Geom2d_Curve, S: Geom_Surface, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
	@overload
	def __init__(self, L: Geom2d_Curve, S: Geom_Surface, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, L: Geom2d_Curve, S: Geom_Surface, P1: gp_Pnt, P2: gp_Pnt, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: Geom2d_Curve, S: Geom_Surface, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float) -> None: ...
	def Edge(self) -> TopoDS_Edge: ...
	def Error(self) -> BRepLib_EdgeError: ...
	def Init(self, C: Geom_Curve) -> None: ...
	def Init(self, C: Geom_Curve, p1: float, p2: float) -> None: ...
	def Init(self, C: Geom_Curve, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
	def Init(self, C: Geom_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	def Init(self, C: Geom_Curve, P1: gp_Pnt, P2: gp_Pnt, p1: float, p2: float) -> None: ...
	def Init(self, C: Geom_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float) -> None: ...
	def Init(self, C: Geom2d_Curve, S: Geom_Surface) -> None: ...
	def Init(self, C: Geom2d_Curve, S: Geom_Surface, p1: float, p2: float) -> None: ...
	def Init(self, C: Geom2d_Curve, S: Geom_Surface, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
	def Init(self, C: Geom2d_Curve, S: Geom_Surface, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	def Init(self, C: Geom2d_Curve, S: Geom_Surface, P1: gp_Pnt, P2: gp_Pnt, p1: float, p2: float) -> None: ...
	def Init(self, C: Geom2d_Curve, S: Geom_Surface, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float) -> None: ...
	def Vertex1(self) -> TopoDS_Vertex: ...
	def Vertex2(self) -> TopoDS_Vertex: ...

class BRepLib_MakeEdge2d(BRepLib_MakeShape):
	@overload
	def __init__(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
	@overload
	def __init__(self, L: gp_Lin2d) -> None: ...
	@overload
	def __init__(self, L: gp_Lin2d, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: gp_Lin2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
	@overload
	def __init__(self, L: gp_Lin2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, L: gp_Circ2d) -> None: ...
	@overload
	def __init__(self, L: gp_Circ2d, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: gp_Circ2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
	@overload
	def __init__(self, L: gp_Circ2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, L: gp_Elips2d) -> None: ...
	@overload
	def __init__(self, L: gp_Elips2d, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: gp_Elips2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
	@overload
	def __init__(self, L: gp_Elips2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, L: gp_Hypr2d) -> None: ...
	@overload
	def __init__(self, L: gp_Hypr2d, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: gp_Hypr2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
	@overload
	def __init__(self, L: gp_Hypr2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, L: gp_Parab2d) -> None: ...
	@overload
	def __init__(self, L: gp_Parab2d, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: gp_Parab2d, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
	@overload
	def __init__(self, L: gp_Parab2d, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, L: Geom2d_Curve) -> None: ...
	@overload
	def __init__(self, L: Geom2d_Curve, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: Geom2d_Curve, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
	@overload
	def __init__(self, L: Geom2d_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, L: Geom2d_Curve, P1: gp_Pnt2d, P2: gp_Pnt2d, p1: float, p2: float) -> None: ...
	@overload
	def __init__(self, L: Geom2d_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float) -> None: ...
	def Edge(self) -> TopoDS_Edge: ...
	def Error(self) -> BRepLib_EdgeError: ...
	def Init(self, C: Geom2d_Curve) -> None: ...
	def Init(self, C: Geom2d_Curve, p1: float, p2: float) -> None: ...
	def Init(self, C: Geom2d_Curve, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
	def Init(self, C: Geom2d_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	def Init(self, C: Geom2d_Curve, P1: gp_Pnt2d, P2: gp_Pnt2d, p1: float, p2: float) -> None: ...
	def Init(self, C: Geom2d_Curve, V1: TopoDS_Vertex, V2: TopoDS_Vertex, p1: float, p2: float) -> None: ...
	def Vertex1(self) -> TopoDS_Vertex: ...
	def Vertex2(self) -> TopoDS_Vertex: ...

class BRepLib_MakeFace(BRepLib_MakeShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, F: TopoDS_Face) -> None: ...
	@overload
	def __init__(self, P: gp_Pln) -> None: ...
	@overload
	def __init__(self, C: gp_Cylinder) -> None: ...
	@overload
	def __init__(self, C: gp_Cone) -> None: ...
	@overload
	def __init__(self, S: gp_Sphere) -> None: ...
	@overload
	def __init__(self, C: gp_Torus) -> None: ...
	@overload
	def __init__(self, S: Geom_Surface, TolDegen: float) -> None: ...
	@overload
	def __init__(self, P: gp_Pln, UMin: float, UMax: float, VMin: float, VMax: float) -> None: ...
	@overload
	def __init__(self, C: gp_Cylinder, UMin: float, UMax: float, VMin: float, VMax: float) -> None: ...
	@overload
	def __init__(self, C: gp_Cone, UMin: float, UMax: float, VMin: float, VMax: float) -> None: ...
	@overload
	def __init__(self, S: gp_Sphere, UMin: float, UMax: float, VMin: float, VMax: float) -> None: ...
	@overload
	def __init__(self, C: gp_Torus, UMin: float, UMax: float, VMin: float, VMax: float) -> None: ...
	@overload
	def __init__(self, S: Geom_Surface, UMin: float, UMax: float, VMin: float, VMax: float, TolDegen: float) -> None: ...
	@overload
	def __init__(self, W: TopoDS_Wire, OnlyPlane: Optional[bool]) -> None: ...
	@overload
	def __init__(self, P: gp_Pln, W: TopoDS_Wire, Inside: Optional[bool]) -> None: ...
	@overload
	def __init__(self, C: gp_Cylinder, W: TopoDS_Wire, Inside: Optional[bool]) -> None: ...
	@overload
	def __init__(self, C: gp_Cone, W: TopoDS_Wire, Inside: Optional[bool]) -> None: ...
	@overload
	def __init__(self, S: gp_Sphere, W: TopoDS_Wire, Inside: Optional[bool]) -> None: ...
	@overload
	def __init__(self, C: gp_Torus, W: TopoDS_Wire, Inside: Optional[bool]) -> None: ...
	@overload
	def __init__(self, S: Geom_Surface, W: TopoDS_Wire, Inside: Optional[bool]) -> None: ...
	@overload
	def __init__(self, F: TopoDS_Face, W: TopoDS_Wire) -> None: ...
	def Add(self, W: TopoDS_Wire) -> None: ...
	def Error(self) -> BRepLib_FaceError: ...
	def Face(self) -> TopoDS_Face: ...
	def Init(self, F: TopoDS_Face) -> None: ...
	def Init(self, S: Geom_Surface, Bound: bool, TolDegen: float) -> None: ...
	def Init(self, S: Geom_Surface, UMin: float, UMax: float, VMin: float, VMax: float, TolDegen: float) -> None: ...
	@staticmethod
	def IsDegenerated(self, theCurve: Geom_Curve, theMaxTol: float) -> Tuple[bool, float]: ...

class BRepLib_MakePolygon(BRepLib_MakeShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, P1: gp_Pnt, P2: gp_Pnt) -> None: ...
	@overload
	def __init__(self, P1: gp_Pnt, P2: gp_Pnt, P3: gp_Pnt, Close: Optional[bool]) -> None: ...
	@overload
	def __init__(self, P1: gp_Pnt, P2: gp_Pnt, P3: gp_Pnt, P4: gp_Pnt, Close: Optional[bool]) -> None: ...
	@overload
	def __init__(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex) -> None: ...
	@overload
	def __init__(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex, V3: TopoDS_Vertex, Close: Optional[bool]) -> None: ...
	@overload
	def __init__(self, V1: TopoDS_Vertex, V2: TopoDS_Vertex, V3: TopoDS_Vertex, V4: TopoDS_Vertex, Close: Optional[bool]) -> None: ...
	def Add(self, P: gp_Pnt) -> None: ...
	def Add(self, V: TopoDS_Vertex) -> None: ...
	def Added(self) -> bool: ...
	def Close(self) -> None: ...
	def Edge(self) -> TopoDS_Edge: ...
	def FirstVertex(self) -> TopoDS_Vertex: ...
	def LastVertex(self) -> TopoDS_Vertex: ...
	def Wire(self) -> TopoDS_Wire: ...

class BRepLib_MakeShell(BRepLib_MakeShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: Geom_Surface, Segment: Optional[bool]) -> None: ...
	@overload
	def __init__(self, S: Geom_Surface, UMin: float, UMax: float, VMin: float, VMax: float, Segment: Optional[bool]) -> None: ...
	def Error(self) -> BRepLib_ShellError: ...
	def Init(self, S: Geom_Surface, UMin: float, UMax: float, VMin: float, VMax: float, Segment: Optional[bool]) -> None: ...
	def Shell(self) -> TopoDS_Shell: ...

class BRepLib_MakeSolid(BRepLib_MakeShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, S: TopoDS_CompSolid) -> None: ...
	@overload
	def __init__(self, S: TopoDS_Shell) -> None: ...
	@overload
	def __init__(self, S1: TopoDS_Shell, S2: TopoDS_Shell) -> None: ...
	@overload
	def __init__(self, S1: TopoDS_Shell, S2: TopoDS_Shell, S3: TopoDS_Shell) -> None: ...
	@overload
	def __init__(self, So: TopoDS_Solid) -> None: ...
	@overload
	def __init__(self, So: TopoDS_Solid, S: TopoDS_Shell) -> None: ...
	def Add(self, S: TopoDS_Shell) -> None: ...
	def FaceStatus(self, F: TopoDS_Face) -> BRepLib_ShapeModification: ...
	def Solid(self) -> TopoDS_Solid: ...

class BRepLib_MakeVertex(BRepLib_MakeShape):
	@overload
	def __init__(self, P: gp_Pnt) -> None: ...
	def Vertex(self) -> TopoDS_Vertex: ...

class BRepLib_MakeWire(BRepLib_MakeShape):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, E: TopoDS_Edge) -> None: ...
	@overload
	def __init__(self, E1: TopoDS_Edge, E2: TopoDS_Edge) -> None: ...
	@overload
	def __init__(self, E1: TopoDS_Edge, E2: TopoDS_Edge, E3: TopoDS_Edge) -> None: ...
	@overload
	def __init__(self, E1: TopoDS_Edge, E2: TopoDS_Edge, E3: TopoDS_Edge, E4: TopoDS_Edge) -> None: ...
	@overload
	def __init__(self, W: TopoDS_Wire) -> None: ...
	@overload
	def __init__(self, W: TopoDS_Wire, E: TopoDS_Edge) -> None: ...
	def Add(self, E: TopoDS_Edge) -> None: ...
	def Add(self, W: TopoDS_Wire) -> None: ...
	def Add(self, L: TopTools_ListOfShape) -> None: ...
	def Edge(self) -> TopoDS_Edge: ...
	def Error(self) -> BRepLib_WireError: ...
	def Vertex(self) -> TopoDS_Vertex: ...
	def Wire(self) -> TopoDS_Wire: ...
