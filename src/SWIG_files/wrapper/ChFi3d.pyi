from typing import overload, NewType, Optional, Tuple

from OCC.Core.ChFi3d import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.TopoDS import *
from OCC.Core.TopAbs import *
from OCC.Core.TopOpeBRepBuild import *
from OCC.Core.Geom import *
from OCC.Core.TopTools import *
from OCC.Core.GeomAbs import *
from OCC.Core.ChFiDS import *
from OCC.Core.Adaptor3d import *
from OCC.Core.math import *
from OCC.Core.Law import *
from OCC.Core.gp import *
from OCC.Core.GeomAdaptor import *
from OCC.Core.TopOpeBRepDS import *
from OCC.Core.Geom2d import *
from OCC.Core.TColStd import *
from OCC.Core.Bnd import *
from OCC.Core.BRepBlend import *
from OCC.Core.IntSurf import *
from OCC.Core.GeomFill import *


class ChFi3d_FilletShape:
	ChFi3d_Rational: int = ...
	ChFi3d_QuasiAngular: int = ...
	ChFi3d_Polynomial: int = ...

class ChFi3d:
	@staticmethod
	def ConcaveSide(self, S1: BRepAdaptor_Surface, S2: BRepAdaptor_Surface, E: TopoDS_Edge, Or1: TopAbs_Orientation, Or2: TopAbs_Orientation) -> int: ...
	@staticmethod
	def NextSide(self, Or1: TopAbs_Orientation, Or2: TopAbs_Orientation, OrSave1: TopAbs_Orientation, OrSave2: TopAbs_Orientation, ChoixSauv: int) -> int: ...
	@staticmethod
	def NextSide(self, Or: TopAbs_Orientation, OrSave: TopAbs_Orientation, OrFace: TopAbs_Orientation) -> None: ...
	@staticmethod
	def SameSide(self, Or: TopAbs_Orientation, OrSave1: TopAbs_Orientation, OrSave2: TopAbs_Orientation, OrFace1: TopAbs_Orientation, OrFace2: TopAbs_Orientation) -> bool: ...

class ChFi3d_Builder:
	def Abscissa(self, IC: int, V: TopoDS_Vertex) -> float: ...
	def BadShape(self) -> TopoDS_Shape: ...
	def Builder(self) -> TopOpeBRepBuild_HBuilder: ...
	def Closed(self, IC: int) -> bool: ...
	def ClosedAndTangent(self, IC: int) -> bool: ...
	def Compute(self) -> None: ...
	def ComputedSurface(self, IC: int, IS: int) -> Geom_Surface: ...
	def Contains(self, E: TopoDS_Edge) -> int: ...
	def Contains(self, E: TopoDS_Edge) -> Tuple[int, int]: ...
	def FaultyContour(self, I: int) -> int: ...
	def FaultyVertex(self, IV: int) -> TopoDS_Vertex: ...
	def FirstVertex(self, IC: int) -> TopoDS_Vertex: ...
	def Generated(self, EouV: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def HasResult(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def LastVertex(self, IC: int) -> TopoDS_Vertex: ...
	def Length(self, IC: int) -> float: ...
	def NbComputedSurfaces(self, IC: int) -> int: ...
	def NbElements(self) -> int: ...
	def NbFaultyContours(self) -> int: ...
	def NbFaultyVertices(self) -> int: ...
	def PerformTwoCornerbyInter(self, Index: int) -> bool: ...
	def RelativeAbscissa(self, IC: int, V: TopoDS_Vertex) -> float: ...
	def Remove(self, E: TopoDS_Edge) -> None: ...
	def Reset(self) -> None: ...
	def SetContinuity(self, InternalContinuity: GeomAbs_Shape, AngularTolerance: float) -> None: ...
	def SetParams(self, Tang: float, Tesp: float, T2d: float, TApp3d: float, TolApp2d: float, Fleche: float) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...
	def SplitKPart(self, Data: ChFiDS_SurfData, SetData: ChFiDS_SequenceOfSurfData, Spine: ChFiDS_Spine, Iedge: int, S1: Adaptor3d_HSurface, I1: Adaptor3d_TopolTool, S2: Adaptor3d_HSurface, I2: Adaptor3d_TopolTool) -> Tuple[bool, bool, bool]: ...
	def StripeStatus(self, IC: int) -> ChFiDS_ErrorStatus: ...
	def Value(self, I: int) -> ChFiDS_Spine: ...

class ChFi3d_SearchSing(math_FunctionWithDerivative):
	def __init__(self, C1: Geom_Curve, C2: Geom_Curve) -> None: ...
	def Derivative(self, X: float) -> Tuple[bool, float]: ...
	def Value(self, X: float) -> Tuple[bool, float]: ...
	def Values(self, X: float) -> Tuple[bool, float, float]: ...

class ChFi3d_ChBuilder(ChFi3d_Builder):
	def __init__(self, S: TopoDS_Shape, Ta: Optional[float]) -> None: ...
	def Add(self, E: TopoDS_Edge) -> None: ...
	def Add(self, Dis: float, E: TopoDS_Edge) -> None: ...
	def Add(self, Dis1: float, Dis2: float, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
	def AddDA(self, Dis: float, Angle: float, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
	def Dists(self, IC: int) -> Tuple[float, float]: ...
	def GetDist(self, IC: int) -> float: ...
	def GetDistAngle(self, IC: int) -> Tuple[float, float]: ...
	def IsChamfer(self, IC: int) -> ChFiDS_ChamfMethod: ...
	def Mode(self) -> ChFiDS_ChamfMode: ...
	def NbSurf(self, IC: int) -> int: ...
	def PerformSurf(self, Data: ChFiDS_SequenceOfSurfData, Guide: ChFiDS_HElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_HSurface, I1: Adaptor3d_TopolTool, S2: BRepAdaptor_HSurface, I2: Adaptor3d_TopolTool, MaxStep: float, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecOnS1: bool, RecOnS2: bool, Soldep: math_Vector) -> Tuple[bool, float, float, int, int]: ...
	def PerformSurf(self, Data: ChFiDS_SequenceOfSurfData, Guide: ChFiDS_HElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_HSurface, I1: Adaptor3d_TopolTool, PC1: BRepAdaptor_HCurve2d, Sref1: BRepAdaptor_HSurface, PCref1: BRepAdaptor_HCurve2d, S2: BRepAdaptor_HSurface, I2: Adaptor3d_TopolTool, Or2: TopAbs_Orientation, MaxStep: float, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP: bool, RecS: bool, RecRst: bool, Soldep: math_Vector) -> Tuple[bool, float, float]: ...
	def PerformSurf(self, Data: ChFiDS_SequenceOfSurfData, Guide: ChFiDS_HElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_HSurface, I1: Adaptor3d_TopolTool, Or1: TopAbs_Orientation, S2: BRepAdaptor_HSurface, I2: Adaptor3d_TopolTool, PC2: BRepAdaptor_HCurve2d, Sref2: BRepAdaptor_HSurface, PCref2: BRepAdaptor_HCurve2d, MaxStep: float, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP: bool, RecS: bool, RecRst: bool, Soldep: math_Vector) -> Tuple[bool, float, float]: ...
	def PerformSurf(self, Data: ChFiDS_SequenceOfSurfData, Guide: ChFiDS_HElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_HSurface, I1: Adaptor3d_TopolTool, PC1: BRepAdaptor_HCurve2d, Sref1: BRepAdaptor_HSurface, PCref1: BRepAdaptor_HCurve2d, Or1: TopAbs_Orientation, S2: BRepAdaptor_HSurface, I2: Adaptor3d_TopolTool, PC2: BRepAdaptor_HCurve2d, Sref2: BRepAdaptor_HSurface, PCref2: BRepAdaptor_HCurve2d, Or2: TopAbs_Orientation, MaxStep: float, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP1: bool, RecRst1: bool, RecP2: bool, RecRst2: bool, Soldep: math_Vector) -> Tuple[bool, bool, float, float]: ...
	def ResetContour(self, IC: int) -> None: ...
	def Sect(self, IC: int, IS: int) -> ChFiDS_SecHArray1: ...
	def SetDist(self, Dis: float, IC: int, F: TopoDS_Face) -> None: ...
	def SetDistAngle(self, Dis: float, Angle: float, IC: int, F: TopoDS_Face) -> None: ...
	def SetDists(self, Dis1: float, Dis2: float, IC: int, F: TopoDS_Face) -> None: ...
	def SetMode(self, theMode: ChFiDS_ChamfMode) -> None: ...
	def SimulSurf(self, Data: ChFiDS_SurfData, Guide: ChFiDS_HElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_HSurface, I1: Adaptor3d_TopolTool, PC1: BRepAdaptor_HCurve2d, Sref1: BRepAdaptor_HSurface, PCref1: BRepAdaptor_HCurve2d, S2: BRepAdaptor_HSurface, I2: Adaptor3d_TopolTool, Or2: TopAbs_Orientation, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP: bool, RecS: bool, RecRst: bool, Soldep: math_Vector) -> Tuple[bool, float, float]: ...
	def SimulSurf(self, Data: ChFiDS_SurfData, Guide: ChFiDS_HElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_HSurface, I1: Adaptor3d_TopolTool, Or1: TopAbs_Orientation, S2: BRepAdaptor_HSurface, I2: Adaptor3d_TopolTool, PC2: BRepAdaptor_HCurve2d, Sref2: BRepAdaptor_HSurface, PCref2: BRepAdaptor_HCurve2d, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP: bool, RecS: bool, RecRst: bool, Soldep: math_Vector) -> Tuple[bool, float, float]: ...
	def SimulSurf(self, Data: ChFiDS_SurfData, Guide: ChFiDS_HElSpine, Spine: ChFiDS_Spine, Choix: int, S1: BRepAdaptor_HSurface, I1: Adaptor3d_TopolTool, PC1: BRepAdaptor_HCurve2d, Sref1: BRepAdaptor_HSurface, PCref1: BRepAdaptor_HCurve2d, Or1: TopAbs_Orientation, S2: BRepAdaptor_HSurface, I2: Adaptor3d_TopolTool, PC2: BRepAdaptor_HCurve2d, Sref2: BRepAdaptor_HSurface, PCref2: BRepAdaptor_HCurve2d, Or2: TopAbs_Orientation, Fleche: float, TolGuide: float, Inside: bool, Appro: bool, Forward: bool, RecP1: bool, RecRst1: bool, RecP2: bool, RecRst2: bool, Soldep: math_Vector) -> Tuple[bool, bool, float, float]: ...
	def Simulate(self, IC: int) -> None: ...

class ChFi3d_FilBuilder(ChFi3d_Builder):
	def __init__(self, S: TopoDS_Shape, FShape: Optional[ChFi3d_FilletShape], Ta: Optional[float]) -> None: ...
	def Add(self, E: TopoDS_Edge) -> None: ...
	def Add(self, Radius: float, E: TopoDS_Edge) -> None: ...
	def GetBounds(self, IC: int, E: TopoDS_Edge) -> Tuple[bool, float, float]: ...
	def GetFilletShape(self) -> ChFi3d_FilletShape: ...
	def GetLaw(self, IC: int, E: TopoDS_Edge) -> Law_Function: ...
	def IsConstant(self, IC: int) -> bool: ...
	def IsConstant(self, IC: int, E: TopoDS_Edge) -> bool: ...
	def NbSurf(self, IC: int) -> int: ...
	def Radius(self, IC: int) -> float: ...
	def Radius(self, IC: int, E: TopoDS_Edge) -> float: ...
	def ResetContour(self, IC: int) -> None: ...
	def Sect(self, IC: int, IS: int) -> ChFiDS_SecHArray1: ...
	def SetFilletShape(self, FShape: ChFi3d_FilletShape) -> None: ...
	def SetLaw(self, IC: int, E: TopoDS_Edge, L: Law_Function) -> None: ...
	def SetRadius(self, C: Law_Function, IC: int, IinC: int) -> None: ...
	def SetRadius(self, Radius: float, IC: int, E: TopoDS_Edge) -> None: ...
	def SetRadius(self, Radius: float, IC: int, V: TopoDS_Vertex) -> None: ...
	def SetRadius(self, UandR: gp_XY, IC: int, IinC: int) -> None: ...
	def Simulate(self, IC: int) -> None: ...
	def UnSet(self, IC: int, E: TopoDS_Edge) -> None: ...
	def UnSet(self, IC: int, V: TopoDS_Vertex) -> None: ...
