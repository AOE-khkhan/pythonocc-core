from typing import overload, NewType, Optional, Tuple

from OCC.Core.AdvApp2Var import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColStd import *
from OCC.Core.GeomAbs import *
from OCC.Core.AdvApprox import *
from OCC.Core.Geom import *
from OCC.Core.gp import *
from OCC.Core.TColgp import *


class AdvApp2Var_CriterionRepartition:
	AdvApp2Var_Regular: int = ...
	AdvApp2Var_Incremental: int = ...

class AdvApp2Var_CriterionType:
	AdvApp2Var_Absolute: int = ...
	AdvApp2Var_Relative: int = ...

class AdvApp2Var_ApproxAFunc2Var:
	@overload
	def __init__(self, Num1DSS: int, Num2DSS: int, Num3DSS: int, OneDTol: TColStd_HArray1OfReal, TwoDTol: TColStd_HArray1OfReal, ThreeDTol: TColStd_HArray1OfReal, OneDTolFr: TColStd_HArray2OfReal, TwoDTolFr: TColStd_HArray2OfReal, ThreeDTolFr: TColStd_HArray2OfReal, FirstInU: float, LastInU: float, FirstInV: float, LastInV: float, FavorIso: GeomAbs_IsoType, ContInU: GeomAbs_Shape, ContInV: GeomAbs_Shape, PrecisCode: int, MaxDegInU: int, MaxDegInV: int, MaxPatch: int, Func: AdvApp2Var_EvaluatorFunc2Var, UChoice: AdvApprox_Cutting, VChoice: AdvApprox_Cutting) -> None: ...
	@overload
	def __init__(self, Num1DSS: int, Num2DSS: int, Num3DSS: int, OneDTol: TColStd_HArray1OfReal, TwoDTol: TColStd_HArray1OfReal, ThreeDTol: TColStd_HArray1OfReal, OneDTolFr: TColStd_HArray2OfReal, TwoDTolFr: TColStd_HArray2OfReal, ThreeDTolFr: TColStd_HArray2OfReal, FirstInU: float, LastInU: float, FirstInV: float, LastInV: float, FavorIso: GeomAbs_IsoType, ContInU: GeomAbs_Shape, ContInV: GeomAbs_Shape, PrecisCode: int, MaxDegInU: int, MaxDegInV: int, MaxPatch: int, Func: AdvApp2Var_EvaluatorFunc2Var, Crit: AdvApp2Var_Criterion, UChoice: AdvApprox_Cutting, VChoice: AdvApprox_Cutting) -> None: ...
	def AverageError(self, Dimension: int) -> TColStd_HArray1OfReal: ...
	def AverageError(self, Dimension: int, Index: int) -> float: ...
	def CritError(self, Dimension: int, Index: int) -> float: ...
	def HasResult(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def MaxError(self, Dimension: int) -> TColStd_HArray1OfReal: ...
	def MaxError(self, Dimension: int, Index: int) -> float: ...
	def NumSubSpaces(self, Dimension: int) -> int: ...
	def Surface(self, Index: int) -> Geom_BSplineSurface: ...
	def UDegree(self) -> int: ...
	def UFrontError(self, Dimension: int) -> TColStd_HArray1OfReal: ...
	def UFrontError(self, Dimension: int, Index: int) -> float: ...
	def VDegree(self) -> int: ...
	def VFrontError(self, Dimension: int) -> TColStd_HArray1OfReal: ...
	def VFrontError(self, Dimension: int, Index: int) -> float: ...

class AdvApp2Var_ApproxF2var:
	pass

class AdvApp2Var_Context:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, ifav: int, iu: int, iv: int, nlimu: int, nlimv: int, iprecis: int, nb1Dss: int, nb2Dss: int, nb3Dss: int, tol1D: TColStd_HArray1OfReal, tol2D: TColStd_HArray1OfReal, tol3D: TColStd_HArray1OfReal, tof1D: TColStd_HArray2OfReal, tof2D: TColStd_HArray2OfReal, tof3D: TColStd_HArray2OfReal) -> None: ...
	def CToler(self) -> TColStd_HArray2OfReal: ...
	def FToler(self) -> TColStd_HArray2OfReal: ...
	def FavorIso(self) -> int: ...
	def IToler(self) -> TColStd_HArray1OfReal: ...
	def TotalDimension(self) -> int: ...
	def TotalNumberSSP(self) -> int: ...
	def UGauss(self) -> TColStd_HArray1OfReal: ...
	def UJacDeg(self) -> int: ...
	def UJacMax(self) -> TColStd_HArray1OfReal: ...
	def ULimit(self) -> int: ...
	def UOrder(self) -> int: ...
	def URoots(self) -> TColStd_HArray1OfReal: ...
	def VGauss(self) -> TColStd_HArray1OfReal: ...
	def VJacDeg(self) -> int: ...
	def VJacMax(self) -> TColStd_HArray1OfReal: ...
	def VLimit(self) -> int: ...
	def VOrder(self) -> int: ...
	def VRoots(self) -> TColStd_HArray1OfReal: ...

class AdvApp2Var_Criterion:
	def IsSatisfied(self, P: AdvApp2Var_Patch) -> bool: ...
	def MaxValue(self) -> float: ...
	def Repartition(self) -> AdvApp2Var_CriterionRepartition: ...
	def Type(self) -> AdvApp2Var_CriterionType: ...
	def Value(self, P: AdvApp2Var_Patch, C: AdvApp2Var_Context) -> None: ...

class AdvApp2Var_Data:
	@staticmethod
	def Getmaovpar(self) -> False: ...
	@staticmethod
	def Getmaovpch(self) -> False: ...
	@staticmethod
	def Getmdnombr(self) -> False: ...
	@staticmethod
	def Getminombr(self) -> False: ...
	@staticmethod
	def Getmlgdrtl(self) -> False: ...
	@staticmethod
	def Getmmapgs0(self) -> False: ...
	@staticmethod
	def Getmmapgs1(self) -> False: ...
	@staticmethod
	def Getmmapgs2(self) -> False: ...
	@staticmethod
	def Getmmapgss(self) -> False: ...
	@staticmethod
	def Getmmcmcnp(self) -> False: ...
	@staticmethod
	def Getmmjcobi(self) -> False: ...

class AdvApp2Var_Framework:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Frame: AdvApp2Var_SequenceOfNode, UFrontier: AdvApp2Var_SequenceOfStrip, VFrontier: AdvApp2Var_SequenceOfStrip) -> None: ...
	def ChangeIso(self, IndexIso: int, IndexStrip: int, anIso: AdvApp2Var_Iso) -> None: ...
	def ChangeNode(self, IndexNode: int) -> AdvApp2Var_Node: ...
	def FirstNode(self, Type: GeomAbs_IsoType, IndexIso: int, IndexStrip: int) -> int: ...
	def FirstNotApprox(self, anIso: AdvApp2Var_Iso) -> Tuple[bool, int, int]: ...
	def IsoU(self, U: float, V0: float, V1: float) -> AdvApp2Var_Iso: ...
	def IsoV(self, U0: float, U1: float, V: float) -> AdvApp2Var_Iso: ...
	def LastNode(self, Type: GeomAbs_IsoType, IndexIso: int, IndexStrip: int) -> int: ...
	def Node(self, IndexNode: int) -> AdvApp2Var_Node: ...
	def Node(self, U: float, V: float) -> AdvApp2Var_Node: ...
	def UEquation(self, IndexIso: int, IndexStrip: int) -> TColStd_HArray1OfReal: ...
	def UpdateInU(self, CuttingValue: float) -> None: ...
	def UpdateInV(self, CuttingValue: float) -> None: ...
	def VEquation(self, IndexIso: int, IndexStrip: int) -> TColStd_HArray1OfReal: ...

class AdvApp2Var_MathBase:
	pass

class AdvApp2Var_Network:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, Net: AdvApp2Var_SequenceOfPatch, TheU: TColStd_SequenceOfReal, TheV: TColStd_SequenceOfReal) -> None: ...
	def ChangePatch(self, Index: int) -> AdvApp2Var_Patch: ...
	def FirstNotApprox(self) -> Tuple[bool, int]: ...
	def NbPatch(self) -> int: ...
	def NbPatchInU(self) -> int: ...
	def NbPatchInV(self) -> int: ...
	def Patch(self, UIndex: int, VIndex: int) -> AdvApp2Var_Patch: ...
	def SameDegree(self, iu: int, iv: int) -> Tuple[int, int]: ...
	def UParameter(self, Index: int) -> float: ...
	def UpdateInU(self, CuttingValue: float) -> None: ...
	def UpdateInV(self, CuttingValue: float) -> None: ...
	def VParameter(self, Index: int) -> float: ...

class AdvApp2Var_Node:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, iu: int, iv: int) -> None: ...
	@overload
	def __init__(self, UV: gp_XY, iu: int, iv: int) -> None: ...
	def Coord(self) -> gp_XY: ...
	def Error(self, iu: int, iv: int) -> float: ...
	def Point(self, iu: int, iv: int) -> gp_Pnt: ...
	def SetCoord(self, x1: float, x2: float) -> None: ...
	def SetError(self, iu: int, iv: int, error: float) -> None: ...
	def SetPoint(self, iu: int, iv: int, Cte: gp_Pnt) -> None: ...
	def UOrder(self) -> int: ...
	def VOrder(self) -> int: ...

class AdvApp2Var_Patch:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, U0: float, U1: float, V0: float, V1: float, iu: int, iv: int) -> None: ...
	def AddConstraints(self, Conditions: AdvApp2Var_Context, Constraints: AdvApp2Var_Framework) -> None: ...
	def AddErrors(self, Constraints: AdvApp2Var_Framework) -> None: ...
	def AverageErrors(self) -> TColStd_HArray1OfReal: ...
	def ChangeDomain(self, a: float, b: float, c: float, d: float) -> None: ...
	def ChangeNbCoeff(self, NbCoeffU: int, NbCoeffV: int) -> None: ...
	def Coefficients(self, SSPIndex: int, Conditions: AdvApp2Var_Context) -> TColStd_HArray1OfReal: ...
	def CritValue(self) -> float: ...
	def CutSense(self) -> int: ...
	def CutSense(self, Crit: AdvApp2Var_Criterion, NumDec: int) -> int: ...
	def Discretise(self, Conditions: AdvApp2Var_Context, Constraints: AdvApp2Var_Framework, func: AdvApp2Var_EvaluatorFunc2Var) -> None: ...
	def HasResult(self) -> bool: ...
	def IsApproximated(self) -> bool: ...
	def IsDiscretised(self) -> bool: ...
	def IsoErrors(self) -> TColStd_HArray2OfReal: ...
	def MakeApprox(self, Conditions: AdvApp2Var_Context, Constraints: AdvApp2Var_Framework, NumDec: int) -> None: ...
	def MaxErrors(self) -> TColStd_HArray1OfReal: ...
	def NbCoeffInU(self) -> int: ...
	def NbCoeffInV(self) -> int: ...
	def OverwriteApprox(self) -> None: ...
	def Poles(self, SSPIndex: int, Conditions: AdvApp2Var_Context) -> TColgp_HArray2OfPnt: ...
	def ResetApprox(self) -> None: ...
	def SetCritValue(self, dist: float) -> None: ...
	def U0(self) -> float: ...
	def U1(self) -> float: ...
	def UOrder(self) -> int: ...
	def V0(self) -> float: ...
	def V1(self) -> float: ...
	def VOrder(self) -> int: ...

class AdvApp2Var_SysBase:
	def __init__(self) -> None: ...
	@staticmethod
	def do__fio(self) -> int: ...
	@staticmethod
	def do__lio(self) -> int: ...
	def mainial_(self) -> False: ...
	@staticmethod
	def mnfndeb_(self) -> int: ...
