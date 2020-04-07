from typing import overload, NewType, Optional, Tuple

from OCC.Core.UnitsAPI import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Units import *


class UnitsAPI_SystemUnits:
	UnitsAPI_DEFAULT: int = ...
	UnitsAPI_SI: int = ...
	UnitsAPI_MDTV: int = ...

class UnitsAPI:
	@staticmethod
	def AnyFromLS(self, aData: float, aUnit: str) -> float: ...
	@staticmethod
	def AnyFromSI(self, aData: float, aUnit: str) -> float: ...
	@staticmethod
	def AnyToAny(self, aData: float, aUnit1: str, aUnit2: str) -> float: ...
	@staticmethod
	def AnyToLS(self, aData: float, aUnit: str) -> float: ...
	@staticmethod
	def AnyToLS(self, aData: float, aUnit: str, aDim: Units_Dimensions) -> float: ...
	@staticmethod
	def AnyToSI(self, aData: float, aUnit: str) -> float: ...
	@staticmethod
	def AnyToSI(self, aData: float, aUnit: str, aDim: Units_Dimensions) -> float: ...
	@staticmethod
	def Check(self, aQuantity: str, aUnit: str) -> bool: ...
	@staticmethod
	def CurrentFromAny(self, aData: float, aQuantity: str, aUnit: str) -> float: ...
	@staticmethod
	def CurrentFromLS(self, aData: float, aQuantity: str) -> float: ...
	@staticmethod
	def CurrentFromSI(self, aData: float, aQuantity: str) -> float: ...
	@staticmethod
	def CurrentToAny(self, aData: float, aQuantity: str, aUnit: str) -> float: ...
	@staticmethod
	def CurrentToLS(self, aData: float, aQuantity: str) -> float: ...
	@staticmethod
	def CurrentToSI(self, aData: float, aQuantity: str) -> float: ...
	@staticmethod
	def CurrentUnit(self, aQuantity: str) -> str: ...
	@staticmethod
	def DimensionAmountOfSubstance(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionElectricCurrent(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionLength(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionLess(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionLuminousIntensity(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionMass(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionPlaneAngle(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionSolidAngle(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionThermodynamicTemperature(self) -> Units_Dimensions: ...
	@staticmethod
	def DimensionTime(self) -> Units_Dimensions: ...
	@staticmethod
	def Dimensions(self, aQuantity: str) -> Units_Dimensions: ...
	@staticmethod
	def LSToSI(self, aData: float, aQuantity: str) -> float: ...
	@staticmethod
	def LocalSystem(self) -> UnitsAPI_SystemUnits: ...
	@staticmethod
	def Reload(self) -> None: ...
	@staticmethod
	def SIToLS(self, aData: float, aQuantity: str) -> float: ...
	@staticmethod
	def Save(self) -> None: ...
	@staticmethod
	def SetCurrentUnit(self, aQuantity: str, aUnit: str) -> None: ...
	@staticmethod
	def SetLocalSystem(self, aSystemUnit: Optional[UnitsAPI_SystemUnits]) -> None: ...
