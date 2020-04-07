from typing import overload, NewType, Optional, Tuple

from OCC.Core.BRep import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TopoDS import *
from OCC.Core.GeomAbs import *
from OCC.Core.Geom import *
from OCC.Core.TopLoc import *
from OCC.Core.Poly import *
from OCC.Core.gp import *
from OCC.Core.Geom2d import *
from OCC.Core.TopAbs import *


class BRep_Builder(TopoDS_Builder):
	def Continuity(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face, C: GeomAbs_Shape) -> None: ...
	def Continuity(self, E: TopoDS_Edge, S1: Geom_Surface, S2: Geom_Surface, L1: TopLoc_Location, L2: TopLoc_Location, C: GeomAbs_Shape) -> None: ...
	def Degenerated(self, E: TopoDS_Edge, D: bool) -> None: ...
	def MakeEdge(self, E: TopoDS_Edge) -> None: ...
	def MakeEdge(self, E: TopoDS_Edge, C: Geom_Curve, Tol: float) -> None: ...
	def MakeEdge(self, E: TopoDS_Edge, C: Geom_Curve, L: TopLoc_Location, Tol: float) -> None: ...
	def MakeEdge(self, E: TopoDS_Edge, P: Poly_Polygon3D) -> None: ...
	def MakeEdge(self, E: TopoDS_Edge, N: Poly_PolygonOnTriangulation, T: Poly_Triangulation) -> None: ...
	def MakeEdge(self, E: TopoDS_Edge, N: Poly_PolygonOnTriangulation, T: Poly_Triangulation, L: TopLoc_Location) -> None: ...
	def MakeFace(self, F: TopoDS_Face) -> None: ...
	def MakeFace(self, F: TopoDS_Face, S: Geom_Surface, Tol: float) -> None: ...
	def MakeFace(self, F: TopoDS_Face, S: Geom_Surface, L: TopLoc_Location, Tol: float) -> None: ...
	def MakeFace(self, F: TopoDS_Face, T: Poly_Triangulation) -> None: ...
	def MakeVertex(self, V: TopoDS_Vertex) -> None: ...
	def MakeVertex(self, V: TopoDS_Vertex, P: gp_Pnt, Tol: float) -> None: ...
	def NaturalRestriction(self, F: TopoDS_Face, N: bool) -> None: ...
	def Range(self, E: TopoDS_Edge, First: float, Last: float, Only3d: Optional[bool]) -> None: ...
	def Range(self, E: TopoDS_Edge, S: Geom_Surface, L: TopLoc_Location, First: float, Last: float) -> None: ...
	def Range(self, E: TopoDS_Edge, F: TopoDS_Face, First: float, Last: float) -> None: ...
	def SameParameter(self, E: TopoDS_Edge, S: bool) -> None: ...
	def SameRange(self, E: TopoDS_Edge, S: bool) -> None: ...
	def Transfert(self, Ein: TopoDS_Edge, Eout: TopoDS_Edge) -> None: ...
	def Transfert(self, Ein: TopoDS_Edge, Eout: TopoDS_Edge, Vin: TopoDS_Vertex, Vout: TopoDS_Vertex) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, C: Geom_Curve, Tol: float) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, C: Geom_Curve, L: TopLoc_Location, Tol: float) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, C: Geom2d_Curve, F: TopoDS_Face, Tol: float) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, C1: Geom2d_Curve, C2: Geom2d_Curve, F: TopoDS_Face, Tol: float) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, C: Geom2d_Curve, S: Geom_Surface, L: TopLoc_Location, Tol: float) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, C: Geom2d_Curve, S: Geom_Surface, L: TopLoc_Location, Tol: float, Pf: gp_Pnt2d, Pl: gp_Pnt2d) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, C1: Geom2d_Curve, C2: Geom2d_Curve, S: Geom_Surface, L: TopLoc_Location, Tol: float) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, C1: Geom2d_Curve, C2: Geom2d_Curve, S: Geom_Surface, L: TopLoc_Location, Tol: float, Pf: gp_Pnt2d, Pl: gp_Pnt2d) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, P: Poly_Polygon3D) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, P: Poly_Polygon3D, L: TopLoc_Location) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, N: Poly_PolygonOnTriangulation, T: Poly_Triangulation) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, N: Poly_PolygonOnTriangulation, T: Poly_Triangulation, L: TopLoc_Location) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, N1: Poly_PolygonOnTriangulation, N2: Poly_PolygonOnTriangulation, T: Poly_Triangulation) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, N1: Poly_PolygonOnTriangulation, N2: Poly_PolygonOnTriangulation, T: Poly_Triangulation, L: TopLoc_Location) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, P: Poly_Polygon2D, S: TopoDS_Face) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, P: Poly_Polygon2D, S: Geom_Surface, T: TopLoc_Location) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, P1: Poly_Polygon2D, P2: Poly_Polygon2D, S: TopoDS_Face) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, P1: Poly_Polygon2D, P2: Poly_Polygon2D, S: Geom_Surface, L: TopLoc_Location) -> None: ...
	def UpdateEdge(self, E: TopoDS_Edge, Tol: float) -> None: ...
	def UpdateFace(self, F: TopoDS_Face, S: Geom_Surface, L: TopLoc_Location, Tol: float) -> None: ...
	def UpdateFace(self, F: TopoDS_Face, T: Poly_Triangulation) -> None: ...
	def UpdateFace(self, F: TopoDS_Face, Tol: float) -> None: ...
	def UpdateVertex(self, V: TopoDS_Vertex, P: gp_Pnt, Tol: float) -> None: ...
	def UpdateVertex(self, V: TopoDS_Vertex, P: float, E: TopoDS_Edge, Tol: float) -> None: ...
	def UpdateVertex(self, V: TopoDS_Vertex, P: float, E: TopoDS_Edge, F: TopoDS_Face, Tol: float) -> None: ...
	def UpdateVertex(self, V: TopoDS_Vertex, P: float, E: TopoDS_Edge, S: Geom_Surface, L: TopLoc_Location, Tol: float) -> None: ...
	def UpdateVertex(self, Ve: TopoDS_Vertex, U: float, V: float, F: TopoDS_Face, Tol: float) -> None: ...
	def UpdateVertex(self, V: TopoDS_Vertex, Tol: float) -> None: ...

class BRep_CurveRepresentation(Standard_Transient):
	def Continuity(self) -> GeomAbs_Shape: ...
	def Continuity(self, C: GeomAbs_Shape) -> None: ...
	def Copy(self) -> BRep_CurveRepresentation: ...
	def Curve3D(self) -> Geom_Curve: ...
	def Curve3D(self, C: Geom_Curve) -> None: ...
	def IsCurve3D(self) -> bool: ...
	def IsCurveOnClosedSurface(self) -> bool: ...
	def IsCurveOnSurface(self) -> bool: ...
	def IsCurveOnSurface(self, S: Geom_Surface, L: TopLoc_Location) -> bool: ...
	def IsPolygon3D(self) -> bool: ...
	def IsPolygonOnClosedSurface(self) -> bool: ...
	def IsPolygonOnClosedTriangulation(self) -> bool: ...
	def IsPolygonOnSurface(self) -> bool: ...
	def IsPolygonOnSurface(self, S: Geom_Surface, L: TopLoc_Location) -> bool: ...
	def IsPolygonOnTriangulation(self) -> bool: ...
	def IsPolygonOnTriangulation(self, T: Poly_Triangulation, L: TopLoc_Location) -> bool: ...
	def IsRegularity(self) -> bool: ...
	def IsRegularity(self, S1: Geom_Surface, S2: Geom_Surface, L1: TopLoc_Location, L2: TopLoc_Location) -> bool: ...
	def Location(self) -> TopLoc_Location: ...
	def Location(self, L: TopLoc_Location) -> None: ...
	def Location2(self) -> TopLoc_Location: ...
	def PCurve(self) -> Geom2d_Curve: ...
	def PCurve(self, C: Geom2d_Curve) -> None: ...
	def PCurve2(self) -> Geom2d_Curve: ...
	def PCurve2(self, C: Geom2d_Curve) -> None: ...
	def Polygon(self) -> Poly_Polygon2D: ...
	def Polygon(self, P: Poly_Polygon2D) -> None: ...
	def Polygon2(self) -> Poly_Polygon2D: ...
	def Polygon2(self, P: Poly_Polygon2D) -> None: ...
	def Polygon3D(self) -> Poly_Polygon3D: ...
	def Polygon3D(self, P: Poly_Polygon3D) -> None: ...
	def PolygonOnTriangulation(self) -> Poly_PolygonOnTriangulation: ...
	def PolygonOnTriangulation(self, P: Poly_PolygonOnTriangulation) -> None: ...
	def PolygonOnTriangulation2(self) -> Poly_PolygonOnTriangulation: ...
	def PolygonOnTriangulation2(self, P2: Poly_PolygonOnTriangulation) -> None: ...
	def Surface(self) -> Geom_Surface: ...
	def Surface2(self) -> Geom_Surface: ...
	def Triangulation(self) -> Poly_Triangulation: ...

class BRep_PointRepresentation(Standard_Transient):
	def Curve(self) -> Geom_Curve: ...
	def Curve(self, C: Geom_Curve) -> None: ...
	def IsPointOnCurve(self) -> bool: ...
	def IsPointOnCurve(self, C: Geom_Curve, L: TopLoc_Location) -> bool: ...
	def IsPointOnCurveOnSurface(self) -> bool: ...
	def IsPointOnCurveOnSurface(self, PC: Geom2d_Curve, S: Geom_Surface, L: TopLoc_Location) -> bool: ...
	def IsPointOnSurface(self) -> bool: ...
	def IsPointOnSurface(self, S: Geom_Surface, L: TopLoc_Location) -> bool: ...
	def Location(self) -> TopLoc_Location: ...
	def Location(self, L: TopLoc_Location) -> None: ...
	def PCurve(self) -> Geom2d_Curve: ...
	def PCurve(self, C: Geom2d_Curve) -> None: ...
	def Parameter(self) -> float: ...
	def Parameter(self, P: float) -> None: ...
	def Parameter2(self) -> float: ...
	def Parameter2(self, P: float) -> None: ...
	def Surface(self) -> Geom_Surface: ...
	def Surface(self, S: Geom_Surface) -> None: ...

class BRep_TEdge(TopoDS_TEdge):
	def __init__(self) -> None: ...
	def ChangeCurves(self) -> BRep_ListOfCurveRepresentation: ...
	def Curves(self) -> BRep_ListOfCurveRepresentation: ...
	def Degenerated(self) -> bool: ...
	def Degenerated(self, S: bool) -> None: ...
	def EmptyCopy(self) -> TopoDS_TShape: ...
	def SameParameter(self) -> bool: ...
	def SameParameter(self, S: bool) -> None: ...
	def SameRange(self) -> bool: ...
	def SameRange(self, S: bool) -> None: ...
	def Tolerance(self) -> float: ...
	def Tolerance(self, T: float) -> None: ...
	def UpdateTolerance(self, T: float) -> None: ...

class BRep_TFace(TopoDS_TFace):
	def __init__(self) -> None: ...
	def EmptyCopy(self) -> TopoDS_TShape: ...
	def Location(self) -> TopLoc_Location: ...
	def Location(self, L: TopLoc_Location) -> None: ...
	def NaturalRestriction(self) -> bool: ...
	def NaturalRestriction(self, N: bool) -> None: ...
	def Surface(self) -> Geom_Surface: ...
	def Surface(self, S: Geom_Surface) -> None: ...
	def Tolerance(self) -> float: ...
	def Tolerance(self, T: float) -> None: ...
	def Triangulation(self) -> Poly_Triangulation: ...
	def Triangulation(self, T: Poly_Triangulation) -> None: ...

class BRep_TVertex(TopoDS_TVertex):
	def __init__(self) -> None: ...
	def ChangePoints(self) -> BRep_ListOfPointRepresentation: ...
	def EmptyCopy(self) -> TopoDS_TShape: ...
	def Pnt(self) -> gp_Pnt: ...
	def Pnt(self, P: gp_Pnt) -> None: ...
	def Points(self) -> BRep_ListOfPointRepresentation: ...
	def Tolerance(self) -> float: ...
	def Tolerance(self, T: float) -> None: ...
	def UpdateTolerance(self, T: float) -> None: ...

class BRep_Tool:
	@staticmethod
	def Continuity(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face) -> GeomAbs_Shape: ...
	@staticmethod
	def Continuity(self, E: TopoDS_Edge, S1: Geom_Surface, S2: Geom_Surface, L1: TopLoc_Location, L2: TopLoc_Location) -> GeomAbs_Shape: ...
	@staticmethod
	def Curve(self, E: TopoDS_Edge, L: TopLoc_Location) -> Tuple[Geom_Curve, float, float]: ...
	@staticmethod
	def Curve(self, E: TopoDS_Edge) -> Tuple[Geom_Curve, float, float]: ...
	@staticmethod
	def CurveOnPlane(self, E: TopoDS_Edge, S: Geom_Surface, L: TopLoc_Location) -> Tuple[Geom2d_Curve, float, float]: ...
	@staticmethod
	def CurveOnSurface(self, E: TopoDS_Edge, F: TopoDS_Face, theIsStored: Optional[bool]) -> Tuple[Geom2d_Curve, float, float]: ...
	@staticmethod
	def CurveOnSurface(self, E: TopoDS_Edge, S: Geom_Surface, L: TopLoc_Location, theIsStored: Optional[bool]) -> Tuple[Geom2d_Curve, float, float]: ...
	@staticmethod
	def CurveOnSurface(self, E: TopoDS_Edge, C: Geom2d_Curve, S: Geom_Surface, L: TopLoc_Location) -> Tuple[float, float]: ...
	@staticmethod
	def CurveOnSurface(self, E: TopoDS_Edge, C: Geom2d_Curve, S: Geom_Surface, L: TopLoc_Location, Index: int) -> Tuple[float, float]: ...
	@staticmethod
	def Degenerated(self, E: TopoDS_Edge) -> bool: ...
	@staticmethod
	def HasContinuity(self, E: TopoDS_Edge, F1: TopoDS_Face, F2: TopoDS_Face) -> bool: ...
	@staticmethod
	def HasContinuity(self, E: TopoDS_Edge, S1: Geom_Surface, S2: Geom_Surface, L1: TopLoc_Location, L2: TopLoc_Location) -> bool: ...
	@staticmethod
	def HasContinuity(self, E: TopoDS_Edge) -> bool: ...
	@staticmethod
	def IsClosed(self, S: TopoDS_Shape) -> bool: ...
	@staticmethod
	def IsClosed(self, E: TopoDS_Edge, F: TopoDS_Face) -> bool: ...
	@staticmethod
	def IsClosed(self, E: TopoDS_Edge, S: Geom_Surface, L: TopLoc_Location) -> bool: ...
	@staticmethod
	def IsClosed(self, E: TopoDS_Edge, T: Poly_Triangulation, L: TopLoc_Location) -> bool: ...
	@staticmethod
	def IsGeometric(self, E: TopoDS_Edge) -> bool: ...
	@staticmethod
	def MaxContinuity(self, theEdge: TopoDS_Edge) -> GeomAbs_Shape: ...
	@staticmethod
	def MaxTolerance(self, theShape: TopoDS_Shape, theSubShape: TopAbs_ShapeEnum) -> float: ...
	@staticmethod
	def NaturalRestriction(self, F: TopoDS_Face) -> bool: ...
	@staticmethod
	def Parameter(self, V: TopoDS_Vertex, E: TopoDS_Edge) -> float: ...
	@staticmethod
	def Parameter(self, V: TopoDS_Vertex, E: TopoDS_Edge, F: TopoDS_Face) -> float: ...
	@staticmethod
	def Parameter(self, V: TopoDS_Vertex, E: TopoDS_Edge, S: Geom_Surface, L: TopLoc_Location) -> float: ...
	@staticmethod
	def Parameters(self, V: TopoDS_Vertex, F: TopoDS_Face) -> gp_Pnt2d: ...
	@staticmethod
	def Pnt(self, V: TopoDS_Vertex) -> gp_Pnt: ...
	@staticmethod
	def Polygon3D(self, E: TopoDS_Edge, L: TopLoc_Location) -> Poly_Polygon3D: ...
	@staticmethod
	def PolygonOnSurface(self, E: TopoDS_Edge, F: TopoDS_Face) -> Poly_Polygon2D: ...
	@staticmethod
	def PolygonOnSurface(self, E: TopoDS_Edge, S: Geom_Surface, L: TopLoc_Location) -> Poly_Polygon2D: ...
	@staticmethod
	def PolygonOnSurface(self, E: TopoDS_Edge, C: Poly_Polygon2D, S: Geom_Surface, L: TopLoc_Location) -> None: ...
	@staticmethod
	def PolygonOnSurface(self, E: TopoDS_Edge, C: Poly_Polygon2D, S: Geom_Surface, L: TopLoc_Location, Index: int) -> None: ...
	@staticmethod
	def PolygonOnTriangulation(self, E: TopoDS_Edge, T: Poly_Triangulation, L: TopLoc_Location) -> Poly_PolygonOnTriangulation: ...
	@staticmethod
	def PolygonOnTriangulation(self, E: TopoDS_Edge, P: Poly_PolygonOnTriangulation, T: Poly_Triangulation, L: TopLoc_Location) -> None: ...
	@staticmethod
	def PolygonOnTriangulation(self, E: TopoDS_Edge, P: Poly_PolygonOnTriangulation, T: Poly_Triangulation, L: TopLoc_Location, Index: int) -> None: ...
	@staticmethod
	def Range(self, E: TopoDS_Edge) -> Tuple[float, float]: ...
	@staticmethod
	def Range(self, E: TopoDS_Edge, S: Geom_Surface, L: TopLoc_Location) -> Tuple[float, float]: ...
	@staticmethod
	def Range(self, E: TopoDS_Edge, F: TopoDS_Face) -> Tuple[float, float]: ...
	@staticmethod
	def SameParameter(self, E: TopoDS_Edge) -> bool: ...
	@staticmethod
	def SameRange(self, E: TopoDS_Edge) -> bool: ...
	@staticmethod
	def SetUVPoints(self, E: TopoDS_Edge, S: Geom_Surface, L: TopLoc_Location, PFirst: gp_Pnt2d, PLast: gp_Pnt2d) -> None: ...
	@staticmethod
	def SetUVPoints(self, E: TopoDS_Edge, F: TopoDS_Face, PFirst: gp_Pnt2d, PLast: gp_Pnt2d) -> None: ...
	@staticmethod
	def Surface(self, F: TopoDS_Face, L: TopLoc_Location) -> Geom_Surface: ...
	@staticmethod
	def Surface(self, F: TopoDS_Face) -> Geom_Surface: ...
	@staticmethod
	def Tolerance(self, F: TopoDS_Face) -> float: ...
	@staticmethod
	def Tolerance(self, E: TopoDS_Edge) -> float: ...
	@staticmethod
	def Tolerance(self, V: TopoDS_Vertex) -> float: ...
	@staticmethod
	def Triangulation(self, F: TopoDS_Face, L: TopLoc_Location) -> Poly_Triangulation: ...
	@staticmethod
	def UVPoints(self, E: TopoDS_Edge, S: Geom_Surface, L: TopLoc_Location, PFirst: gp_Pnt2d, PLast: gp_Pnt2d) -> None: ...
	@staticmethod
	def UVPoints(self, E: TopoDS_Edge, F: TopoDS_Face, PFirst: gp_Pnt2d, PLast: gp_Pnt2d) -> None: ...

class BRep_CurveOn2Surfaces(BRep_CurveRepresentation):
	def __init__(self, S1: Geom_Surface, S2: Geom_Surface, L1: TopLoc_Location, L2: TopLoc_Location, C: GeomAbs_Shape) -> None: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def Continuity(self, C: GeomAbs_Shape) -> None: ...
	def Copy(self) -> BRep_CurveRepresentation: ...
	def D0(self, U: float, P: gp_Pnt) -> None: ...
	def IsRegularity(self) -> bool: ...
	def IsRegularity(self, S1: Geom_Surface, S2: Geom_Surface, L1: TopLoc_Location, L2: TopLoc_Location) -> bool: ...
	def Location2(self) -> TopLoc_Location: ...
	def Surface(self) -> Geom_Surface: ...
	def Surface2(self) -> Geom_Surface: ...

class BRep_GCurve(BRep_CurveRepresentation):
	def D0(self, U: float, P: gp_Pnt) -> None: ...
	def First(self) -> float: ...
	def First(self, F: float) -> None: ...
	def Last(self) -> float: ...
	def Last(self, L: float) -> None: ...
	def Range(self) -> Tuple[float, float]: ...
	def SetRange(self, First: float, Last: float) -> None: ...
	def Update(self) -> None: ...

class BRep_PointOnCurve(BRep_PointRepresentation):
	def __init__(self, P: float, C: Geom_Curve, L: TopLoc_Location) -> None: ...
	def Curve(self) -> Geom_Curve: ...
	def Curve(self, C: Geom_Curve) -> None: ...
	def IsPointOnCurve(self) -> bool: ...
	def IsPointOnCurve(self, C: Geom_Curve, L: TopLoc_Location) -> bool: ...

class BRep_PointsOnSurface(BRep_PointRepresentation):
	def Surface(self) -> Geom_Surface: ...
	def Surface(self, S: Geom_Surface) -> None: ...

class BRep_Polygon3D(BRep_CurveRepresentation):
	def __init__(self, P: Poly_Polygon3D, L: TopLoc_Location) -> None: ...
	def Copy(self) -> BRep_CurveRepresentation: ...
	def IsPolygon3D(self) -> bool: ...
	def Polygon3D(self) -> Poly_Polygon3D: ...
	def Polygon3D(self, P: Poly_Polygon3D) -> None: ...

class BRep_PolygonOnSurface(BRep_CurveRepresentation):
	def __init__(self, P: Poly_Polygon2D, S: Geom_Surface, L: TopLoc_Location) -> None: ...
	def Copy(self) -> BRep_CurveRepresentation: ...
	def IsPolygonOnSurface(self) -> bool: ...
	def IsPolygonOnSurface(self, S: Geom_Surface, L: TopLoc_Location) -> bool: ...
	def Polygon(self) -> Poly_Polygon2D: ...
	def Polygon(self, P: Poly_Polygon2D) -> None: ...
	def Surface(self) -> Geom_Surface: ...

class BRep_PolygonOnTriangulation(BRep_CurveRepresentation):
	def __init__(self, P: Poly_PolygonOnTriangulation, T: Poly_Triangulation, L: TopLoc_Location) -> None: ...
	def Copy(self) -> BRep_CurveRepresentation: ...
	def IsPolygonOnTriangulation(self) -> bool: ...
	def IsPolygonOnTriangulation(self, T: Poly_Triangulation, L: TopLoc_Location) -> bool: ...
	def PolygonOnTriangulation(self, P: Poly_PolygonOnTriangulation) -> None: ...
	def PolygonOnTriangulation(self) -> Poly_PolygonOnTriangulation: ...
	def Triangulation(self) -> Poly_Triangulation: ...

class BRep_Curve3D(BRep_GCurve):
	def __init__(self, C: Geom_Curve, L: TopLoc_Location) -> None: ...
	def Copy(self) -> BRep_CurveRepresentation: ...
	def Curve3D(self) -> Geom_Curve: ...
	def Curve3D(self, C: Geom_Curve) -> None: ...
	def D0(self, U: float, P: gp_Pnt) -> None: ...
	def IsCurve3D(self) -> bool: ...

class BRep_CurveOnSurface(BRep_GCurve):
	def __init__(self, PC: Geom2d_Curve, S: Geom_Surface, L: TopLoc_Location) -> None: ...
	def Copy(self) -> BRep_CurveRepresentation: ...
	def D0(self, U: float, P: gp_Pnt) -> None: ...
	def IsCurveOnSurface(self) -> bool: ...
	def IsCurveOnSurface(self, S: Geom_Surface, L: TopLoc_Location) -> bool: ...
	def PCurve(self) -> Geom2d_Curve: ...
	def PCurve(self, C: Geom2d_Curve) -> None: ...
	def SetUVPoints(self, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
	def Surface(self) -> Geom_Surface: ...
	def UVPoints(self, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
	def Update(self) -> None: ...

class BRep_PointOnCurveOnSurface(BRep_PointsOnSurface):
	def __init__(self, P: float, C: Geom2d_Curve, S: Geom_Surface, L: TopLoc_Location) -> None: ...
	def IsPointOnCurveOnSurface(self) -> bool: ...
	def IsPointOnCurveOnSurface(self, PC: Geom2d_Curve, S: Geom_Surface, L: TopLoc_Location) -> bool: ...
	def PCurve(self) -> Geom2d_Curve: ...
	def PCurve(self, C: Geom2d_Curve) -> None: ...

class BRep_PointOnSurface(BRep_PointsOnSurface):
	def __init__(self, P1: float, P2: float, S: Geom_Surface, L: TopLoc_Location) -> None: ...
	def IsPointOnSurface(self) -> bool: ...
	def IsPointOnSurface(self, S: Geom_Surface, L: TopLoc_Location) -> bool: ...
	def Parameter2(self) -> float: ...
	def Parameter2(self, P: float) -> None: ...

class BRep_PolygonOnClosedSurface(BRep_PolygonOnSurface):
	def __init__(self, P1: Poly_Polygon2D, P2: Poly_Polygon2D, S: Geom_Surface, L: TopLoc_Location) -> None: ...
	def Copy(self) -> BRep_CurveRepresentation: ...
	def IsPolygonOnClosedSurface(self) -> bool: ...
	def Polygon2(self) -> Poly_Polygon2D: ...
	def Polygon2(self, P: Poly_Polygon2D) -> None: ...

class BRep_PolygonOnClosedTriangulation(BRep_PolygonOnTriangulation):
	def __init__(self, P1: Poly_PolygonOnTriangulation, P2: Poly_PolygonOnTriangulation, Tr: Poly_Triangulation, L: TopLoc_Location) -> None: ...
	def Copy(self) -> BRep_CurveRepresentation: ...
	def IsPolygonOnClosedTriangulation(self) -> bool: ...
	def PolygonOnTriangulation2(self, P2: Poly_PolygonOnTriangulation) -> None: ...
	def PolygonOnTriangulation2(self) -> Poly_PolygonOnTriangulation: ...

class BRep_CurveOnClosedSurface(BRep_CurveOnSurface):
	def __init__(self, PC1: Geom2d_Curve, PC2: Geom2d_Curve, S: Geom_Surface, L: TopLoc_Location, C: GeomAbs_Shape) -> None: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def Continuity(self, C: GeomAbs_Shape) -> None: ...
	def Copy(self) -> BRep_CurveRepresentation: ...
	def IsCurveOnClosedSurface(self) -> bool: ...
	def IsRegularity(self) -> bool: ...
	def IsRegularity(self, S1: Geom_Surface, S2: Geom_Surface, L1: TopLoc_Location, L2: TopLoc_Location) -> bool: ...
	def Location2(self) -> TopLoc_Location: ...
	def PCurve2(self) -> Geom2d_Curve: ...
	def PCurve2(self, C: Geom2d_Curve) -> None: ...
	def SetUVPoints2(self, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
	def Surface2(self) -> Geom_Surface: ...
	def UVPoints2(self, P1: gp_Pnt2d, P2: gp_Pnt2d) -> None: ...
	def Update(self) -> None: ...
