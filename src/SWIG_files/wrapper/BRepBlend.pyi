from typing import overload, NewType, Optional, Tuple

from OCC.Core.BRepBlend import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BlendFunc import *
from OCC.Core.Approx import *
from OCC.Core.gp import *
from OCC.Core.TColgp import *
from OCC.Core.TColStd import *
from OCC.Core.GeomAbs import *
from OCC.Core.Blend import *
from OCC.Core.math import *
from OCC.Core.AppBlend import *
from OCC.Core.Adaptor3d import *
from OCC.Core.Adaptor2d import *
from OCC.Core.IntSurf import *
from OCC.Core.Law import *
from OCC.Core.ChFiDS import *
from OCC.Core.TopAbs import *

BRepBlend_CSCircular = NewType('BRepBlend_CSCircular', BlendFunc_CSCircular)
BRepBlend_CSConstRad = NewType('BRepBlend_CSConstRad', BlendFunc_CSConstRad)
BRepBlend_ChAsym = NewType('BRepBlend_ChAsym', BlendFunc_ChAsym)
BRepBlend_ChAsymInv = NewType('BRepBlend_ChAsymInv', BlendFunc_ChAsymInv)
BRepBlend_ChamfInv = NewType('BRepBlend_ChamfInv', BlendFunc_ChamfInv)
BRepBlend_Chamfer = NewType('BRepBlend_Chamfer', BlendFunc_Chamfer)
BRepBlend_ConstRad = NewType('BRepBlend_ConstRad', BlendFunc_ConstRad)
BRepBlend_ConstRadInv = NewType('BRepBlend_ConstRadInv', BlendFunc_ConstRadInv)
BRepBlend_ConstThroat = NewType('BRepBlend_ConstThroat', BlendFunc_ConstThroat)
BRepBlend_ConstThroatInv = NewType('BRepBlend_ConstThroatInv', BlendFunc_ConstThroatInv)
BRepBlend_ConstThroatWithPenetration = NewType('BRepBlend_ConstThroatWithPenetration', BlendFunc_ConstThroatWithPenetration)
BRepBlend_ConstThroatWithPenetrationInv = NewType('BRepBlend_ConstThroatWithPenetrationInv', BlendFunc_ConstThroatWithPenetrationInv)
BRepBlend_EvolRad = NewType('BRepBlend_EvolRad', BlendFunc_EvolRad)
BRepBlend_EvolRadInv = NewType('BRepBlend_EvolRadInv', BlendFunc_EvolRadInv)
BRepBlend_Ruled = NewType('BRepBlend_Ruled', BlendFunc_Ruled)
BRepBlend_RuledInv = NewType('BRepBlend_RuledInv', BlendFunc_RuledInv)

class BRepBlend_AppFuncRoot(Approx_SweepFunction):
	def BarycentreOfSurf(self) -> gp_Pnt: ...
	def D0(self, Param: float, First: float, Last: float, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> bool: ...
	def D1(self, Param: float, First: float, Last: float, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
	def D2(self, Param: float, First: float, Last: float, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
	def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
	def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: TColStd_Array1OfReal) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsRational(self) -> bool: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def MaximalSection(self) -> float: ...
	def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
	def Nb2dCurves(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def Point(self, Func: Blend_AppFunction, Param: float, Sol: math_Vector, Pnt: Blend_Point) -> None: ...
	def Resolution(self, Index: int, Tol: float) -> Tuple[float, float]: ...
	def SectionShape(self) -> Tuple[int, int, int]: ...
	def SetInterval(self, First: float, Last: float) -> None: ...
	def SetTolerance(self, Tol3d: float, Tol2d: float) -> None: ...
	def Vec(self, Sol: math_Vector, Pnt: Blend_Point) -> None: ...

class BRepBlend_AppSurf(AppBlend_Approx):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Degmin: int, Degmax: int, Tol3d: float, Tol2d: float, NbIt: int, KnownParameters: Optional[bool]) -> None: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def CriteriumWeight(self) -> Tuple[float, float, float]: ...
	def Curve2d(self, Index: int, TPoles: TColgp_Array1OfPnt2d, TKnots: TColStd_Array1OfReal, TMults: TColStd_Array1OfInteger) -> None: ...
	def Curve2dPoles(self, Index: int) -> TColgp_Array1OfPnt2d: ...
	def Curves2dDegree(self) -> int: ...
	def Curves2dKnots(self) -> TColStd_Array1OfReal: ...
	def Curves2dMults(self) -> TColStd_Array1OfInteger: ...
	def Curves2dShape(self) -> Tuple[int, int, int]: ...
	def Init(self, Degmin: int, Degmax: int, Tol3d: float, Tol2d: float, NbIt: int, KnownParameters: Optional[bool]) -> None: ...
	def IsDone(self) -> bool: ...
	def NbCurves2d(self) -> int: ...
	def ParType(self) -> Approx_ParametrizationType: ...
	def Perform(self, Lin: BRepBlend_Line, SecGen: Blend_AppFunction, SpApprox: Optional[bool]) -> None: ...
	def Perform(self, Lin: BRepBlend_Line, SecGen: Blend_AppFunction, NbMaxP: int) -> None: ...
	def PerformSmoothing(self, Lin: BRepBlend_Line, SecGen: Blend_AppFunction) -> None: ...
	def SetContinuity(self, C: GeomAbs_Shape) -> None: ...
	def SetCriteriumWeight(self, W1: float, W2: float, W3: float) -> None: ...
	def SetParType(self, ParType: Approx_ParametrizationType) -> None: ...
	def SurfPoles(self) -> TColgp_Array2OfPnt: ...
	def SurfShape(self) -> Tuple[int, int, int, int, int, int]: ...
	def SurfUKnots(self) -> TColStd_Array1OfReal: ...
	def SurfUMults(self) -> TColStd_Array1OfInteger: ...
	def SurfVKnots(self) -> TColStd_Array1OfReal: ...
	def SurfVMults(self) -> TColStd_Array1OfInteger: ...
	def SurfWeights(self) -> TColStd_Array2OfReal: ...
	def Surface(self, TPoles: TColgp_Array2OfPnt, TWeights: TColStd_Array2OfReal, TUKnots: TColStd_Array1OfReal, TVKnots: TColStd_Array1OfReal, TUMults: TColStd_Array1OfInteger, TVMults: TColStd_Array1OfInteger) -> None: ...
	def TolCurveOnSurf(self, Index: int) -> float: ...
	def TolReached(self) -> Tuple[float, float]: ...
	def UDegree(self) -> int: ...
	def VDegree(self) -> int: ...

class BRepBlend_AppSurface(AppBlend_Approx):
	def __init__(self, Funct: Approx_SweepFunction, First: float, Last: float, Tol3d: float, Tol2d: float, TolAngular: float, Continuity: Optional[GeomAbs_Shape], Degmax: Optional[int], Segmax: Optional[int]) -> None: ...
	def Curve2d(self, Index: int, TPoles: TColgp_Array1OfPnt2d, TKnots: TColStd_Array1OfReal, TMults: TColStd_Array1OfInteger) -> None: ...
	def Curve2dPoles(self, Index: int) -> TColgp_Array1OfPnt2d: ...
	def Curves2dDegree(self) -> int: ...
	def Curves2dKnots(self) -> TColStd_Array1OfReal: ...
	def Curves2dMults(self) -> TColStd_Array1OfInteger: ...
	def Curves2dShape(self) -> Tuple[int, int, int]: ...
	def IsDone(self) -> bool: ...
	def Max2dError(self, Index: int) -> float: ...
	def MaxErrorOnSurf(self) -> float: ...
	def NbCurves2d(self) -> int: ...
	def SurfPoles(self) -> TColgp_Array2OfPnt: ...
	def SurfShape(self) -> Tuple[int, int, int, int, int, int]: ...
	def SurfUKnots(self) -> TColStd_Array1OfReal: ...
	def SurfUMults(self) -> TColStd_Array1OfInteger: ...
	def SurfVKnots(self) -> TColStd_Array1OfReal: ...
	def SurfVMults(self) -> TColStd_Array1OfInteger: ...
	def SurfWeights(self) -> TColStd_Array2OfReal: ...
	def Surface(self, TPoles: TColgp_Array2OfPnt, TWeights: TColStd_Array2OfReal, TUKnots: TColStd_Array1OfReal, TVKnots: TColStd_Array1OfReal, TUMults: TColStd_Array1OfInteger, TVMults: TColStd_Array1OfInteger) -> None: ...
	def TolCurveOnSurf(self, Index: int) -> float: ...
	def UDegree(self) -> int: ...
	def VDegree(self) -> int: ...

class BRepBlend_CSWalking:
	def __init__(self, Curv: Adaptor3d_HCurve, Surf: Adaptor3d_HSurface, Domain: Adaptor3d_TopolTool) -> None: ...
	def Complete(self, F: Blend_CSFunction, Pmin: float) -> bool: ...
	def IsDone(self) -> bool: ...
	def Line(self) -> BRepBlend_Line: ...
	def Perform(self, F: Blend_CSFunction, Pdep: float, Pmax: float, MaxStep: float, TolGuide: float, Soldep: math_Vector, Tolesp: float, Fleche: float, Appro: Optional[bool]) -> None: ...

class BRepBlend_CurvPointRadInv(Blend_CurvPointFuncInv):
	def __init__(self, C1: Adaptor3d_HCurve, C2: Adaptor3d_HCurve) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def NbEquations(self) -> int: ...
	def Set(self, Choix: int) -> None: ...
	def Set(self, P: gp_Pnt) -> None: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BRepBlend_Extremity:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, P: gp_Pnt, U: float, V: float, Param: float, Tol: float) -> None: ...
	@overload
	def __init__(self, P: gp_Pnt, U: float, V: float, Param: float, Tol: float, Vtx: Adaptor3d_HVertex) -> None: ...
	@overload
	def __init__(self, P: gp_Pnt, W: float, Param: float, Tol: float) -> None: ...
	def AddArc(self, A: Adaptor2d_HCurve2d, Param: float, TLine: IntSurf_Transition, TArc: IntSurf_Transition) -> None: ...
	def HasTangent(self) -> bool: ...
	def IsVertex(self) -> bool: ...
	def NbPointOnRst(self) -> int: ...
	def Parameter(self) -> float: ...
	def ParameterOnGuide(self) -> float: ...
	def Parameters(self) -> Tuple[float, float]: ...
	def PointOnRst(self, Index: int) -> BRepBlend_PointOnRst: ...
	def SetTangent(self, Tangent: gp_Vec) -> None: ...
	def SetValue(self, P: gp_Pnt, U: float, V: float, Param: float, Tol: float) -> None: ...
	def SetValue(self, P: gp_Pnt, U: float, V: float, Param: float, Tol: float, Vtx: Adaptor3d_HVertex) -> None: ...
	def SetValue(self, P: gp_Pnt, W: float, Param: float, Tol: float) -> None: ...
	def SetVertex(self, V: Adaptor3d_HVertex) -> None: ...
	def Tangent(self) -> gp_Vec: ...
	def Tolerance(self) -> float: ...
	def Value(self) -> gp_Pnt: ...
	def Vertex(self) -> Adaptor3d_HVertex: ...

class BRepBlend_Line(Standard_Transient):
	def __init__(self) -> None: ...
	def Append(self, P: Blend_Point) -> None: ...
	def Clear(self) -> None: ...
	def EndPointOnFirst(self) -> BRepBlend_Extremity: ...
	def EndPointOnSecond(self) -> BRepBlend_Extremity: ...
	def InsertBefore(self, Index: int, P: Blend_Point) -> None: ...
	def NbPoints(self) -> int: ...
	def Point(self, Index: int) -> Blend_Point: ...
	def Prepend(self, P: Blend_Point) -> None: ...
	def Remove(self, FromIndex: int, ToIndex: int) -> None: ...
	def Set(self, TranS1: IntSurf_TypeTrans, TranS2: IntSurf_TypeTrans) -> None: ...
	def Set(self, Trans: IntSurf_TypeTrans) -> None: ...
	def SetEndPoints(self, EndPt1: BRepBlend_Extremity, EndPt2: BRepBlend_Extremity) -> None: ...
	def SetStartPoints(self, StartPt1: BRepBlend_Extremity, StartPt2: BRepBlend_Extremity) -> None: ...
	def StartPointOnFirst(self) -> BRepBlend_Extremity: ...
	def StartPointOnSecond(self) -> BRepBlend_Extremity: ...
	def TransitionOnS(self) -> IntSurf_TypeTrans: ...
	def TransitionOnS1(self) -> IntSurf_TypeTrans: ...
	def TransitionOnS2(self) -> IntSurf_TypeTrans: ...

class BRepBlend_PointOnRst:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, A: Adaptor2d_HCurve2d, Param: float, TLine: IntSurf_Transition, TArc: IntSurf_Transition) -> None: ...
	def Arc(self) -> Adaptor2d_HCurve2d: ...
	def ParameterOnArc(self) -> float: ...
	def SetArc(self, A: Adaptor2d_HCurve2d, Param: float, TLine: IntSurf_Transition, TArc: IntSurf_Transition) -> None: ...
	def TransitionOnArc(self) -> IntSurf_Transition: ...
	def TransitionOnLine(self) -> IntSurf_Transition: ...

class BRepBlend_RstRstConstRad(Blend_RstRstFunction):
	def __init__(self, Surf1: Adaptor3d_HSurface, Rst1: Adaptor2d_HCurve2d, Surf2: Adaptor3d_HSurface, Rst2: Adaptor2d_HCurve2d, CGuide: Adaptor3d_HCurve) -> None: ...
	def CenterCircleRst1Rst2(self, PtRst1: gp_Pnt, PtRst2: gp_Pnt, np: gp_Vec, Center: gp_Pnt, VdMed: gp_Vec) -> bool: ...
	def Decroch(self, Sol: math_Vector, NRst1: gp_Vec, TgRst1: gp_Vec, NRst2: gp_Vec, TgRst2: gp_Vec) -> Blend_DecrochStatus: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetMinimalDistance(self) -> float: ...
	def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
	def GetSectionSize(self) -> float: ...
	def GetShape(self) -> Tuple[int, int, int, int]: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsRational(self) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
	def NbEquations(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbVariables(self) -> int: ...
	def ParameterOnRst1(self) -> float: ...
	def ParameterOnRst2(self) -> float: ...
	def Pnt2dOnRst1(self) -> gp_Pnt2d: ...
	def Pnt2dOnRst2(self) -> gp_Pnt2d: ...
	def PointOnRst1(self) -> gp_Pnt: ...
	def PointOnRst2(self) -> gp_Pnt: ...
	def Resolution(self, IC2d: int, Tol: float) -> Tuple[float, float]: ...
	def Section(self, Param: float, U: float, V: float, C: gp_Circ) -> Tuple[float, float]: ...
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
	def Set(self, SurfRef1: Adaptor3d_HSurface, RstRef1: Adaptor2d_HCurve2d, SurfRef2: Adaptor3d_HSurface, RstRef2: Adaptor2d_HCurve2d) -> None: ...
	def Set(self, Param: float) -> None: ...
	def Set(self, First: float, Last: float) -> None: ...
	def Set(self, Radius: float, Choix: int) -> None: ...
	def Set(self, TypeSection: BlendFunc_SectionShape) -> None: ...
	def Tangent2dOnRst1(self) -> gp_Vec2d: ...
	def Tangent2dOnRst2(self) -> gp_Vec2d: ...
	def TangentOnRst1(self) -> gp_Vec: ...
	def TangentOnRst2(self) -> gp_Vec: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BRepBlend_RstRstEvolRad(Blend_RstRstFunction):
	def __init__(self, Surf1: Adaptor3d_HSurface, Rst1: Adaptor2d_HCurve2d, Surf2: Adaptor3d_HSurface, Rst2: Adaptor2d_HCurve2d, CGuide: Adaptor3d_HCurve, Evol: Law_Function) -> None: ...
	def CenterCircleRst1Rst2(self, PtRst1: gp_Pnt, PtRst2: gp_Pnt, np: gp_Vec, Center: gp_Pnt, VdMed: gp_Vec) -> bool: ...
	def Decroch(self, Sol: math_Vector, NRst1: gp_Vec, TgRst1: gp_Vec, NRst2: gp_Vec, TgRst2: gp_Vec) -> Blend_DecrochStatus: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetMinimalDistance(self) -> float: ...
	def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
	def GetSectionSize(self) -> float: ...
	def GetShape(self) -> Tuple[int, int, int, int]: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsRational(self) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
	def NbEquations(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbVariables(self) -> int: ...
	def ParameterOnRst1(self) -> float: ...
	def ParameterOnRst2(self) -> float: ...
	def Pnt2dOnRst1(self) -> gp_Pnt2d: ...
	def Pnt2dOnRst2(self) -> gp_Pnt2d: ...
	def PointOnRst1(self) -> gp_Pnt: ...
	def PointOnRst2(self) -> gp_Pnt: ...
	def Resolution(self, IC2d: int, Tol: float) -> Tuple[float, float]: ...
	def Section(self, Param: float, U: float, V: float, C: gp_Circ) -> Tuple[float, float]: ...
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
	def Set(self, SurfRef1: Adaptor3d_HSurface, RstRef1: Adaptor2d_HCurve2d, SurfRef2: Adaptor3d_HSurface, RstRef2: Adaptor2d_HCurve2d) -> None: ...
	def Set(self, Param: float) -> None: ...
	def Set(self, First: float, Last: float) -> None: ...
	def Set(self, Choix: int) -> None: ...
	def Set(self, TypeSection: BlendFunc_SectionShape) -> None: ...
	def Tangent2dOnRst1(self) -> gp_Vec2d: ...
	def Tangent2dOnRst2(self) -> gp_Vec2d: ...
	def TangentOnRst1(self) -> gp_Vec: ...
	def TangentOnRst2(self) -> gp_Vec: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BRepBlend_RstRstLineBuilder:
	def __init__(self, Surf1: Adaptor3d_HSurface, Rst1: Adaptor2d_HCurve2d, Domain1: Adaptor3d_TopolTool, Surf2: Adaptor3d_HSurface, Rst2: Adaptor2d_HCurve2d, Domain2: Adaptor3d_TopolTool) -> None: ...
	def Complete(self, Func: Blend_RstRstFunction, Finv1: Blend_SurfCurvFuncInv, FinvP1: Blend_CurvPointFuncInv, Finv2: Blend_SurfCurvFuncInv, FinvP2: Blend_CurvPointFuncInv, Pmin: float) -> bool: ...
	def Decroch1End(self) -> bool: ...
	def Decroch1Start(self) -> bool: ...
	def Decroch2End(self) -> bool: ...
	def Decroch2Start(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def Line(self) -> BRepBlend_Line: ...
	def Perform(self, Func: Blend_RstRstFunction, Finv1: Blend_SurfCurvFuncInv, FinvP1: Blend_CurvPointFuncInv, Finv2: Blend_SurfCurvFuncInv, FinvP2: Blend_CurvPointFuncInv, Pdep: float, Pmax: float, MaxStep: float, TolGuide: float, Soldep: math_Vector, Tolesp: float, Fleche: float, Appro: Optional[bool]) -> None: ...
	def PerformFirstSection(self, Func: Blend_RstRstFunction, Finv1: Blend_SurfCurvFuncInv, FinvP1: Blend_CurvPointFuncInv, Finv2: Blend_SurfCurvFuncInv, FinvP2: Blend_CurvPointFuncInv, Pdep: float, Pmax: float, Soldep: math_Vector, Tolesp: float, TolGuide: float, RecRst1: bool, RecP1: bool, RecRst2: bool, RecP2: bool, ParSol: math_Vector) -> Tuple[bool, float]: ...

class BRepBlend_SurfCurvConstRadInv(Blend_SurfCurvFuncInv):
	def __init__(self, S: Adaptor3d_HSurface, C: Adaptor3d_HCurve, Cg: Adaptor3d_HCurve) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def NbEquations(self) -> int: ...
	def Set(self, R: float, Choix: int) -> None: ...
	def Set(self, Rst: Adaptor2d_HCurve2d) -> None: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BRepBlend_SurfCurvEvolRadInv(Blend_SurfCurvFuncInv):
	def __init__(self, S: Adaptor3d_HSurface, C: Adaptor3d_HCurve, Cg: Adaptor3d_HCurve, Evol: Law_Function) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def NbEquations(self) -> int: ...
	def Set(self, Choix: int) -> None: ...
	def Set(self, Rst: Adaptor2d_HCurve2d) -> None: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BRepBlend_SurfPointConstRadInv(Blend_SurfPointFuncInv):
	def __init__(self, S: Adaptor3d_HSurface, C: Adaptor3d_HCurve) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def NbEquations(self) -> int: ...
	def Set(self, R: float, Choix: int) -> None: ...
	def Set(self, P: gp_Pnt) -> None: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BRepBlend_SurfPointEvolRadInv(Blend_SurfPointFuncInv):
	def __init__(self, S: Adaptor3d_HSurface, C: Adaptor3d_HCurve, Evol: Law_Function) -> None: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def NbEquations(self) -> int: ...
	def Set(self, Choix: int) -> None: ...
	def Set(self, P: gp_Pnt) -> None: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BRepBlend_SurfRstConstRad(Blend_SurfRstFunction):
	def __init__(self, Surf: Adaptor3d_HSurface, SurfRst: Adaptor3d_HSurface, Rst: Adaptor2d_HCurve2d, CGuide: Adaptor3d_HCurve) -> None: ...
	def Decroch(self, Sol: math_Vector, NS: gp_Vec, TgS: gp_Vec) -> bool: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetMinimalDistance(self) -> float: ...
	def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
	def GetSectionSize(self) -> float: ...
	def GetShape(self) -> Tuple[int, int, int, int]: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsRational(self) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
	def NbEquations(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbVariables(self) -> int: ...
	def ParameterOnRst(self) -> float: ...
	def Pnt2dOnRst(self) -> gp_Pnt2d: ...
	def Pnt2dOnS(self) -> gp_Pnt2d: ...
	def PointOnRst(self) -> gp_Pnt: ...
	def PointOnS(self) -> gp_Pnt: ...
	def Resolution(self, IC2d: int, Tol: float) -> Tuple[float, float]: ...
	def Section(self, Param: float, U: float, V: float, W: float, C: gp_Circ) -> Tuple[float, float]: ...
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
	def Set(self, SurfRef: Adaptor3d_HSurface, RstRef: Adaptor2d_HCurve2d) -> None: ...
	def Set(self, Param: float) -> None: ...
	def Set(self, First: float, Last: float) -> None: ...
	def Set(self, Radius: float, Choix: int) -> None: ...
	def Set(self, TypeSection: BlendFunc_SectionShape) -> None: ...
	def Tangent2dOnRst(self) -> gp_Vec2d: ...
	def Tangent2dOnS(self) -> gp_Vec2d: ...
	def TangentOnRst(self) -> gp_Vec: ...
	def TangentOnS(self) -> gp_Vec: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BRepBlend_SurfRstEvolRad(Blend_SurfRstFunction):
	def __init__(self, Surf: Adaptor3d_HSurface, SurfRst: Adaptor3d_HSurface, Rst: Adaptor2d_HCurve2d, CGuide: Adaptor3d_HCurve, Evol: Law_Function) -> None: ...
	def Decroch(self, Sol: math_Vector, NS: gp_Vec, TgS: gp_Vec) -> bool: ...
	def Derivatives(self, X: math_Vector, D: math_Matrix) -> bool: ...
	def GetBounds(self, InfBound: math_Vector, SupBound: math_Vector) -> None: ...
	def GetMinimalDistance(self) -> float: ...
	def GetMinimalWeight(self, Weigths: TColStd_Array1OfReal) -> None: ...
	def GetSectionSize(self) -> float: ...
	def GetShape(self) -> Tuple[int, int, int, int]: ...
	def GetTolerance(self, Tolerance: math_Vector, Tol: float) -> None: ...
	def GetTolerance(self, BoundTol: float, SurfTol: float, AngleTol: float, Tol3d: math_Vector, Tol1D: math_Vector) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsRational(self) -> bool: ...
	def IsSolution(self, Sol: math_Vector, Tol: float) -> bool: ...
	def IsTangencyPoint(self) -> bool: ...
	def Knots(self, TKnots: TColStd_Array1OfReal) -> None: ...
	def Mults(self, TMults: TColStd_Array1OfInteger) -> None: ...
	def NbEquations(self) -> int: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbVariables(self) -> int: ...
	def ParameterOnRst(self) -> float: ...
	def Pnt2dOnRst(self) -> gp_Pnt2d: ...
	def Pnt2dOnS(self) -> gp_Pnt2d: ...
	def PointOnRst(self) -> gp_Pnt: ...
	def PointOnS(self) -> gp_Pnt: ...
	def Resolution(self, IC2d: int, Tol: float) -> Tuple[float, float]: ...
	def Section(self, Param: float, U: float, V: float, W: float, C: gp_Circ) -> Tuple[float, float]: ...
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal) -> bool: ...
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, DPoles: TColgp_Array1OfVec, D2Poles: TColgp_Array1OfVec, Poles2d: TColgp_Array1OfPnt2d, DPoles2d: TColgp_Array1OfVec2d, D2Poles2d: TColgp_Array1OfVec2d, Weigths: TColStd_Array1OfReal, DWeigths: TColStd_Array1OfReal, D2Weigths: TColStd_Array1OfReal) -> bool: ...
	def Section(self, P: Blend_Point, Poles: TColgp_Array1OfPnt, Poles2d: TColgp_Array1OfPnt2d, Weigths: TColStd_Array1OfReal) -> None: ...
	def Set(self, SurfRef: Adaptor3d_HSurface, RstRef: Adaptor2d_HCurve2d) -> None: ...
	def Set(self, Param: float) -> None: ...
	def Set(self, First: float, Last: float) -> None: ...
	def Set(self, Choix: int) -> None: ...
	def Set(self, TypeSection: BlendFunc_SectionShape) -> None: ...
	def Tangent2dOnRst(self) -> gp_Vec2d: ...
	def Tangent2dOnS(self) -> gp_Vec2d: ...
	def TangentOnRst(self) -> gp_Vec: ...
	def TangentOnS(self) -> gp_Vec: ...
	def Value(self, X: math_Vector, F: math_Vector) -> bool: ...
	def Values(self, X: math_Vector, F: math_Vector, D: math_Matrix) -> bool: ...

class BRepBlend_SurfRstLineBuilder:
	def __init__(self, Surf1: Adaptor3d_HSurface, Domain1: Adaptor3d_TopolTool, Surf2: Adaptor3d_HSurface, Rst: Adaptor2d_HCurve2d, Domain2: Adaptor3d_TopolTool) -> None: ...
	def ArcToRecadre(self, Sol: math_Vector, PrevIndex: int, pt2d: gp_Pnt2d, lastpt2d: gp_Pnt2d) -> Tuple[int, float]: ...
	def Complete(self, Func: Blend_SurfRstFunction, Finv: Blend_FuncInv, FinvP: Blend_SurfPointFuncInv, FinvC: Blend_SurfCurvFuncInv, Pmin: float) -> bool: ...
	def DecrochEnd(self) -> bool: ...
	def DecrochStart(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def Line(self) -> BRepBlend_Line: ...
	def Perform(self, Func: Blend_SurfRstFunction, Finv: Blend_FuncInv, FinvP: Blend_SurfPointFuncInv, FinvC: Blend_SurfCurvFuncInv, Pdep: float, Pmax: float, MaxStep: float, TolGuide: float, Soldep: math_Vector, Tolesp: float, Fleche: float, Appro: Optional[bool]) -> None: ...
	def PerformFirstSection(self, Func: Blend_SurfRstFunction, Finv: Blend_FuncInv, FinvP: Blend_SurfPointFuncInv, FinvC: Blend_SurfCurvFuncInv, Pdep: float, Pmax: float, Soldep: math_Vector, Tolesp: float, TolGuide: float, RecRst: bool, RecP: bool, RecS: bool, ParSol: math_Vector) -> Tuple[bool, float]: ...

class BRepBlend_Walking:
	def __init__(self, Surf1: Adaptor3d_HSurface, Surf2: Adaptor3d_HSurface, Domain1: Adaptor3d_TopolTool, Domain2: Adaptor3d_TopolTool, HGuide: ChFiDS_HElSpine) -> None: ...
	def AddSingularPoint(self, P: Blend_Point) -> None: ...
	def Check(self, C: bool) -> None: ...
	def Check2d(self, C: bool) -> None: ...
	def ClassificationOnS1(self, C: bool) -> None: ...
	def ClassificationOnS2(self, C: bool) -> None: ...
	def Complete(self, F: Blend_Function, FInv: Blend_FuncInv, Pmin: float) -> bool: ...
	def Continu(self, F: Blend_Function, FInv: Blend_FuncInv, P: float) -> bool: ...
	def Continu(self, F: Blend_Function, FInv: Blend_FuncInv, P: float, OnS1: bool) -> bool: ...
	def IsDone(self) -> bool: ...
	def Line(self) -> BRepBlend_Line: ...
	def Perform(self, F: Blend_Function, FInv: Blend_FuncInv, Pdep: float, Pmax: float, MaxStep: float, TolGuide: float, Soldep: math_Vector, Tolesp: float, Fleche: float, Appro: Optional[bool]) -> None: ...
	def PerformFirstSection(self, F: Blend_Function, Pdep: float, ParDep: math_Vector, Tolesp: float, TolGuide: float, Pos1: TopAbs_State, Pos2: TopAbs_State) -> bool: ...
	def PerformFirstSection(self, F: Blend_Function, FInv: Blend_FuncInv, Pdep: float, Pmax: float, ParDep: math_Vector, Tolesp: float, TolGuide: float, RecOnS1: bool, RecOnS2: bool, ParSol: math_Vector) -> Tuple[bool, float]: ...
	def SetDomainsToRecadre(self, RecDomain1: Adaptor3d_TopolTool, RecDomain2: Adaptor3d_TopolTool) -> None: ...
	def TwistOnS1(self) -> bool: ...
	def TwistOnS2(self) -> bool: ...

class BRepBlend_AppFunc(BRepBlend_AppFuncRoot):
	def __init__(self, Line: BRepBlend_Line, Func: Blend_Function, Tol3d: float, Tol2d: float) -> None: ...
	def Point(self, Func: Blend_AppFunction, Param: float, Sol: math_Vector, Pnt: Blend_Point) -> None: ...
	def Vec(self, Sol: math_Vector, Pnt: Blend_Point) -> None: ...

class BRepBlend_AppFuncRst(BRepBlend_AppFuncRoot):
	def __init__(self, Line: BRepBlend_Line, Func: Blend_SurfRstFunction, Tol3d: float, Tol2d: float) -> None: ...
	def Point(self, Func: Blend_AppFunction, Param: float, Sol: math_Vector, Pnt: Blend_Point) -> None: ...
	def Vec(self, Sol: math_Vector, Pnt: Blend_Point) -> None: ...

class BRepBlend_AppFuncRstRst(BRepBlend_AppFuncRoot):
	def __init__(self, Line: BRepBlend_Line, Func: Blend_RstRstFunction, Tol3d: float, Tol2d: float) -> None: ...
	def Point(self, Func: Blend_AppFunction, Param: float, Sol: math_Vector, Pnt: Blend_Point) -> None: ...
	def Vec(self, Sol: math_Vector, Pnt: Blend_Point) -> None: ...
