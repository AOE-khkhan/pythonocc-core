from typing import overload, NewType, Optional, Tuple

from OCC.Core.PLib import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColgp import *
from OCC.Core.TColStd import *
from OCC.Core.GeomAbs import *
from OCC.Core.math import *


class PLib:
	@staticmethod
	def Bin(self, N: int, P: int) -> float: ...
	@staticmethod
	def CoefficientsPoles(self, Coefs: TColgp_Array1OfPnt, WCoefs: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt, WPoles: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def CoefficientsPoles(self, Coefs: TColgp_Array1OfPnt2d, WCoefs: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt2d, WPoles: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def CoefficientsPoles(self, Coefs: TColStd_Array1OfReal, WCoefs: TColStd_Array1OfReal, Poles: TColStd_Array1OfReal, WPoles: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def CoefficientsPoles(self, dim: int, Coefs: TColStd_Array1OfReal, WCoefs: TColStd_Array1OfReal, Poles: TColStd_Array1OfReal, WPoles: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def CoefficientsPoles(self, Coefs: TColgp_Array2OfPnt, WCoefs: TColStd_Array2OfReal, Poles: TColgp_Array2OfPnt, WPoles: TColStd_Array2OfReal) -> None: ...
	@staticmethod
	def ConstraintOrder(self, NivConstr: int) -> GeomAbs_Shape: ...
	@staticmethod
	def EvalCubicHermite(self, U: float, DerivativeOrder: int, Dimension: int) -> Tuple[int, float, float, float, float]: ...
	@staticmethod
	def EvalLagrange(self, U: float, DerivativeOrder: int, Degree: int, Dimension: int) -> Tuple[int, float, float, float]: ...
	@staticmethod
	def EvalLength(self, Degree: int, Dimension: int, U1: float, U2: float) -> Tuple[float, float]: ...
	@staticmethod
	def EvalLength(self, Degree: int, Dimension: int, U1: float, U2: float, Tol: float) -> Tuple[float, float, float]: ...
	@staticmethod
	def EvalPoly2Var(self, U: float, V: float, UDerivativeOrder: int, VDerivativeOrder: int, UDegree: int, VDegree: int, Dimension: int) -> Tuple[float, float]: ...
	@staticmethod
	def EvalPolynomial(self, U: float, DerivativeOrder: int, Degree: int, Dimension: int) -> Tuple[float, float]: ...
	@staticmethod
	def GetPoles(self, FP: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt) -> None: ...
	@staticmethod
	def GetPoles(self, FP: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def GetPoles(self, FP: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt2d) -> None: ...
	@staticmethod
	def GetPoles(self, FP: TColStd_Array1OfReal, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def HermiteCoefficients(self, FirstParameter: float, LastParameter: float, FirstOrder: int, LastOrder: int, MatrixCoefs: math_Matrix) -> bool: ...
	@staticmethod
	def HermiteInterpolate(self, Dimension: int, FirstParameter: float, LastParameter: float, FirstOrder: int, LastOrder: int, FirstConstr: TColStd_Array2OfReal, LastConstr: TColStd_Array2OfReal, Coefficients: TColStd_Array1OfReal) -> bool: ...
	@staticmethod
	def JacobiParameters(self, ConstraintOrder: GeomAbs_Shape, MaxDegree: int, Code: int) -> Tuple[int, int]: ...
	@staticmethod
	def NivConstr(self, ConstraintOrder: GeomAbs_Shape) -> int: ...
	@staticmethod
	def NoDerivativeEvalPolynomial(self, U: float, Degree: int, Dimension: int, DegreeDimension: int) -> Tuple[float, float]: ...
	@staticmethod
	def NoWeights(self) -> TColStd_Array1OfReal: ...
	@staticmethod
	def NoWeights2(self) -> TColStd_Array2OfReal: ...
	@staticmethod
	def RationalDerivative(self, Degree: int, N: int, Dimension: int, All: Optional[bool]) -> Tuple[float, float]: ...
	@staticmethod
	def RationalDerivatives(self, DerivativesRequest: int, Dimension: int) -> Tuple[float, float, float]: ...
	@staticmethod
	def SetPoles(self, Poles: TColgp_Array1OfPnt, FP: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def SetPoles(self, Poles: TColgp_Array1OfPnt, Weights: TColStd_Array1OfReal, FP: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def SetPoles(self, Poles: TColgp_Array1OfPnt2d, FP: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def SetPoles(self, Poles: TColgp_Array1OfPnt2d, Weights: TColStd_Array1OfReal, FP: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def Trimming(self, U1: float, U2: float, Coeffs: TColgp_Array1OfPnt, WCoeffs: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def Trimming(self, U1: float, U2: float, Coeffs: TColgp_Array1OfPnt2d, WCoeffs: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def Trimming(self, U1: float, U2: float, Coeffs: TColStd_Array1OfReal, WCoeffs: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def Trimming(self, U1: float, U2: float, dim: int, Coeffs: TColStd_Array1OfReal, WCoeffs: TColStd_Array1OfReal) -> None: ...
	@staticmethod
	def UTrimming(self, U1: float, U2: float, Coeffs: TColgp_Array2OfPnt, WCoeffs: TColStd_Array2OfReal) -> None: ...
	@staticmethod
	def VTrimming(self, V1: float, V2: float, Coeffs: TColgp_Array2OfPnt, WCoeffs: TColStd_Array2OfReal) -> None: ...

class PLib_Base(Standard_Transient):
	def D0(self, U: float, BasisValue: TColStd_Array1OfReal) -> None: ...
	def D1(self, U: float, BasisValue: TColStd_Array1OfReal, BasisD1: TColStd_Array1OfReal) -> None: ...
	def D2(self, U: float, BasisValue: TColStd_Array1OfReal, BasisD1: TColStd_Array1OfReal, BasisD2: TColStd_Array1OfReal) -> None: ...
	def D3(self, U: float, BasisValue: TColStd_Array1OfReal, BasisD1: TColStd_Array1OfReal, BasisD2: TColStd_Array1OfReal, BasisD3: TColStd_Array1OfReal) -> None: ...
	def ReduceDegree(self, Dimension: int, MaxDegree: int, Tol: float) -> Tuple[float, int, float]: ...
	def ToCoefficients(self, Dimension: int, Degree: int, CoeffinBase: TColStd_Array1OfReal, Coefficients: TColStd_Array1OfReal) -> None: ...
	def WorkDegree(self) -> int: ...

class PLib_DoubleJacobiPolynomial:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, JacPolU: PLib_JacobiPolynomial, JacPolV: PLib_JacobiPolynomial) -> None: ...
	def AverageError(self, Dimension: int, DegreeU: int, DegreeV: int, dJacCoeff: int, JacCoeff: TColStd_Array1OfReal) -> float: ...
	def MaxError(self, Dimension: int, MinDegreeU: int, MaxDegreeU: int, MinDegreeV: int, MaxDegreeV: int, dJacCoeff: int, JacCoeff: TColStd_Array1OfReal, Error: float) -> float: ...
	def MaxErrorU(self, Dimension: int, DegreeU: int, DegreeV: int, dJacCoeff: int, JacCoeff: TColStd_Array1OfReal) -> float: ...
	def MaxErrorV(self, Dimension: int, DegreeU: int, DegreeV: int, dJacCoeff: int, JacCoeff: TColStd_Array1OfReal) -> float: ...
	def ReduceDegree(self, Dimension: int, MinDegreeU: int, MaxDegreeU: int, MinDegreeV: int, MaxDegreeV: int, dJacCoeff: int, JacCoeff: TColStd_Array1OfReal, EpmsCut: float) -> Tuple[float, int, int]: ...
	def TabMaxU(self) -> TColStd_HArray1OfReal: ...
	def TabMaxV(self) -> TColStd_HArray1OfReal: ...
	def U(self) -> PLib_JacobiPolynomial: ...
	def V(self) -> PLib_JacobiPolynomial: ...
	def WDoubleJacobiToCoefficients(self, Dimension: int, DegreeU: int, DegreeV: int, JacCoeff: TColStd_Array1OfReal, Coefficients: TColStd_Array1OfReal) -> None: ...

class PLib_HermitJacobi(PLib_Base):
	def __init__(self, WorkDegree: int, ConstraintOrder: GeomAbs_Shape) -> None: ...
	def AverageError(self, Dimension: int, NewDegree: int) -> Tuple[float, float]: ...
	def D0(self, U: float, BasisValue: TColStd_Array1OfReal) -> None: ...
	def D1(self, U: float, BasisValue: TColStd_Array1OfReal, BasisD1: TColStd_Array1OfReal) -> None: ...
	def D2(self, U: float, BasisValue: TColStd_Array1OfReal, BasisD1: TColStd_Array1OfReal, BasisD2: TColStd_Array1OfReal) -> None: ...
	def D3(self, U: float, BasisValue: TColStd_Array1OfReal, BasisD1: TColStd_Array1OfReal, BasisD2: TColStd_Array1OfReal, BasisD3: TColStd_Array1OfReal) -> None: ...
	def MaxError(self, Dimension: int, NewDegree: int) -> Tuple[float, float]: ...
	def NivConstr(self) -> int: ...
	def ReduceDegree(self, Dimension: int, MaxDegree: int, Tol: float) -> Tuple[float, int, float]: ...
	def ToCoefficients(self, Dimension: int, Degree: int, HermJacCoeff: TColStd_Array1OfReal, Coefficients: TColStd_Array1OfReal) -> None: ...
	def WorkDegree(self) -> int: ...

class PLib_JacobiPolynomial(PLib_Base):
	def __init__(self, WorkDegree: int, ConstraintOrder: GeomAbs_Shape) -> None: ...
	def AverageError(self, Dimension: int, NewDegree: int) -> Tuple[float, float]: ...
	def D0(self, U: float, BasisValue: TColStd_Array1OfReal) -> None: ...
	def D1(self, U: float, BasisValue: TColStd_Array1OfReal, BasisD1: TColStd_Array1OfReal) -> None: ...
	def D2(self, U: float, BasisValue: TColStd_Array1OfReal, BasisD1: TColStd_Array1OfReal, BasisD2: TColStd_Array1OfReal) -> None: ...
	def D3(self, U: float, BasisValue: TColStd_Array1OfReal, BasisD1: TColStd_Array1OfReal, BasisD2: TColStd_Array1OfReal, BasisD3: TColStd_Array1OfReal) -> None: ...
	def MaxError(self, Dimension: int, NewDegree: int) -> Tuple[float, float]: ...
	def MaxValue(self, TabMax: TColStd_Array1OfReal) -> None: ...
	def NivConstr(self) -> int: ...
	def Points(self, NbGaussPoints: int, TabPoints: TColStd_Array1OfReal) -> None: ...
	def ReduceDegree(self, Dimension: int, MaxDegree: int, Tol: float) -> Tuple[float, int, float]: ...
	def ToCoefficients(self, Dimension: int, Degree: int, JacCoeff: TColStd_Array1OfReal, Coefficients: TColStd_Array1OfReal) -> None: ...
	def Weights(self, NbGaussPoints: int, TabWeights: TColStd_Array2OfReal) -> None: ...
	def WorkDegree(self) -> int: ...
