from typing import overload, NewType, Optional, Tuple

from OCC.Core.Prs3d import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColgp import *
from OCC.Core.Graphic3d import *
from OCC.Core.TopoDS import *
from OCC.Core.gp import *
from OCC.Core.TCollection import *
from OCC.Core.GeomAbs import *
from OCC.Core.Aspect import *
from OCC.Core.HLRAlgo import *
from OCC.Core.TopLoc import *
from OCC.Core.Poly import *
from OCC.Core.Bnd import *
from OCC.Core.TopTools import *
from OCC.Core.Quantity import *
from OCC.Core.TColStd import *

Graphic3d_HighlightStyle = NewType('Graphic3d_HighlightStyle', Prs3d_Drawer)
Prs3d_Presentation = NewType('Prs3d_Presentation', Graphic3d_Structure)

class Prs3d_DimensionTextVerticalPosition:
	Prs3d_DTVP_Above: int = ...
	Prs3d_DTVP_Below: int = ...
	Prs3d_DTVP_Center: int = ...

class Prs3d_TypeOfHighlight:
	Prs3d_TypeOfHighlight_None: int = ...
	Prs3d_TypeOfHighlight_Selected: int = ...
	Prs3d_TypeOfHighlight_Dynamic: int = ...
	Prs3d_TypeOfHighlight_LocalSelected: int = ...
	Prs3d_TypeOfHighlight_LocalDynamic: int = ...
	Prs3d_TypeOfHighlight_SubIntensity: int = ...
	Prs3d_TypeOfHighlight_NB: int = ...

class Prs3d_VertexDrawMode:
	Prs3d_VDM_Isolated: int = ...
	Prs3d_VDM_All: int = ...
	Prs3d_VDM_Inherited: int = ...

class Prs3d_DatumMode:
	Prs3d_DM_WireFrame: int = ...
	Prs3d_DM_Shaded: int = ...

class Prs3d_DatumAttribute:
	Prs3d_DA_XAxisLength: int = ...
	Prs3d_DA_YAxisLength: int = ...
	Prs3d_DA_ZAxisLength: int = ...
	Prs3d_DP_ShadingTubeRadiusPercent: int = ...
	Prs3d_DP_ShadingConeRadiusPercent: int = ...
	Prs3d_DP_ShadingConeLengthPercent: int = ...
	Prs3d_DP_ShadingOriginRadiusPercent: int = ...
	Prs3d_DP_ShadingNumberOfFacettes: int = ...

class Prs3d_DimensionTextHorizontalPosition:
	Prs3d_DTHP_Left: int = ...
	Prs3d_DTHP_Right: int = ...
	Prs3d_DTHP_Center: int = ...
	Prs3d_DTHP_Fit: int = ...

class Prs3d_TypeOfLinePicking:
	Prs3d_TOLP_Point: int = ...
	Prs3d_TOLP_Segment: int = ...

class Prs3d_TypeOfHLR:
	Prs3d_TOH_NotSet: int = ...
	Prs3d_TOH_PolyAlgo: int = ...
	Prs3d_TOH_Algo: int = ...

class Prs3d_DatumAxes:
	Prs3d_DA_XAxis: int = ...
	Prs3d_DA_YAxis: int = ...
	Prs3d_DA_ZAxis: int = ...
	Prs3d_DA_XYAxis: int = ...
	Prs3d_DA_YZAxis: int = ...
	Prs3d_DA_XZAxis: int = ...
	Prs3d_DA_XYZAxis: int = ...

class Prs3d_DatumParts:
	Prs3d_DP_Origin: int = ...
	Prs3d_DP_XAxis: int = ...
	Prs3d_DP_YAxis: int = ...
	Prs3d_DP_ZAxis: int = ...
	Prs3d_DP_XArrow: int = ...
	Prs3d_DP_YArrow: int = ...
	Prs3d_DP_ZArrow: int = ...
	Prs3d_DP_XOYAxis: int = ...
	Prs3d_DP_YOZAxis: int = ...
	Prs3d_DP_XOZAxis: int = ...
	Prs3d_DP_None: int = ...

class Prs3d_DimensionArrowOrientation:
	Prs3d_DAO_Internal: int = ...
	Prs3d_DAO_External: int = ...
	Prs3d_DAO_Fit: int = ...

class Prs3d:
	@staticmethod
	def AddPrimitivesGroup(self, thePrs: Prs3d_Presentation, theAspect: Prs3d_LineAspect, thePolylines: Prs3d_NListOfSequenceOfPnt) -> None: ...
	@staticmethod
	def GetDeflection(self, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer) -> float: ...
	@staticmethod
	def MatchSegment(self, X: float, Y: float, Z: float, aDistance: float, p1: gp_Pnt, p2: gp_Pnt) -> Tuple[bool, float]: ...
	@staticmethod
	def PrimitivesFromPolylines(self, thePoints: Prs3d_NListOfSequenceOfPnt) -> Graphic3d_ArrayOfPrimitives: ...

class Prs3d_BasicAspect(Standard_Transient):
	pass

class Prs3d_DimensionUnits:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theUnits: Prs3d_DimensionUnits) -> None: ...
	def GetAngleUnits(self) -> TCollection_AsciiString: ...
	def GetLengthUnits(self) -> TCollection_AsciiString: ...
	def SetAngleUnits(self, theUnits: TCollection_AsciiString) -> None: ...
	def SetLengthUnits(self, theUnits: TCollection_AsciiString) -> None: ...

class Prs3d_Drawer(Graphic3d_PresentationAttributes):
	def __init__(self) -> None: ...
	def ArrowAspect(self) -> Prs3d_ArrowAspect: ...
	def ClearLocalAttributes(self) -> None: ...
	def DatumAspect(self) -> Prs3d_DatumAspect: ...
	def DeviationAngle(self) -> float: ...
	def DeviationCoefficient(self) -> float: ...
	def DimAngleDisplayUnits(self) -> TCollection_AsciiString: ...
	def DimAngleModelUnits(self) -> TCollection_AsciiString: ...
	def DimLengthDisplayUnits(self) -> TCollection_AsciiString: ...
	def DimLengthModelUnits(self) -> TCollection_AsciiString: ...
	def DimensionAspect(self) -> Prs3d_DimensionAspect: ...
	def DisableDrawHiddenLine(self) -> None: ...
	def Discretisation(self) -> int: ...
	def DrawHiddenLine(self) -> bool: ...
	def EnableDrawHiddenLine(self) -> None: ...
	def FaceBoundaryAspect(self) -> Prs3d_LineAspect: ...
	def FaceBoundaryDraw(self) -> bool: ...
	def FaceBoundaryUpperContinuity(self) -> GeomAbs_Shape: ...
	def FreeBoundaryAspect(self) -> Prs3d_LineAspect: ...
	def FreeBoundaryDraw(self) -> bool: ...
	def HLRAngle(self) -> float: ...
	def HLRDeviationCoefficient(self) -> float: ...
	def HasLink(self) -> bool: ...
	def HasOwnArrowAspect(self) -> bool: ...
	def HasOwnDatumAspect(self) -> bool: ...
	def HasOwnDeviationAngle(self) -> bool: ...
	def HasOwnDeviationCoefficient(self) -> bool: ...
	def HasOwnDimAngleDisplayUnits(self) -> bool: ...
	def HasOwnDimAngleModelUnits(self) -> bool: ...
	def HasOwnDimLengthDisplayUnits(self) -> bool: ...
	def HasOwnDimLengthModelUnits(self) -> bool: ...
	def HasOwnDimensionAspect(self) -> bool: ...
	def HasOwnDiscretisation(self) -> bool: ...
	def HasOwnDrawHiddenLine(self) -> bool: ...
	def HasOwnFaceBoundaryAspect(self) -> bool: ...
	def HasOwnFaceBoundaryDraw(self) -> bool: ...
	def HasOwnFaceBoundaryUpperContinuity(self) -> bool: ...
	def HasOwnFreeBoundaryAspect(self) -> bool: ...
	def HasOwnFreeBoundaryDraw(self) -> bool: ...
	def HasOwnHLRDeviationAngle(self) -> bool: ...
	def HasOwnHLRDeviationCoefficient(self) -> bool: ...
	def HasOwnHiddenLineAspect(self) -> bool: ...
	def HasOwnIsAutoTriangulation(self) -> bool: ...
	def HasOwnIsoOnPlane(self) -> bool: ...
	def HasOwnIsoOnTriangulation(self) -> bool: ...
	def HasOwnLineArrowDraw(self) -> bool: ...
	def HasOwnLineAspect(self) -> bool: ...
	def HasOwnMaximalChordialDeviation(self) -> bool: ...
	def HasOwnMaximalParameterValue(self) -> bool: ...
	def HasOwnPlaneAspect(self) -> bool: ...
	def HasOwnPointAspect(self) -> bool: ...
	def HasOwnSectionAspect(self) -> bool: ...
	def HasOwnSeenLineAspect(self) -> bool: ...
	def HasOwnShadingAspect(self) -> bool: ...
	def HasOwnTextAspect(self) -> bool: ...
	def HasOwnTypeOfDeflection(self) -> bool: ...
	def HasOwnTypeOfHLR(self) -> bool: ...
	def HasOwnUIsoAspect(self) -> bool: ...
	def HasOwnUnFreeBoundaryAspect(self) -> bool: ...
	def HasOwnUnFreeBoundaryDraw(self) -> bool: ...
	def HasOwnVIsoAspect(self) -> bool: ...
	def HasOwnVectorAspect(self) -> bool: ...
	def HasOwnVertexDrawMode(self) -> bool: ...
	def HasOwnWireAspect(self) -> bool: ...
	def HasOwnWireDraw(self) -> bool: ...
	def HiddenLineAspect(self) -> Prs3d_LineAspect: ...
	def IsAutoTriangulation(self) -> bool: ...
	def IsoOnPlane(self) -> bool: ...
	def IsoOnTriangulation(self) -> bool: ...
	def LineArrowDraw(self) -> bool: ...
	def LineAspect(self) -> Prs3d_LineAspect: ...
	def Link(self) -> Prs3d_Drawer: ...
	def Link(self, theDrawer: Prs3d_Drawer) -> None: ...
	def MaximalChordialDeviation(self) -> float: ...
	def MaximalParameterValue(self) -> float: ...
	def PlaneAspect(self) -> Prs3d_PlaneAspect: ...
	def PointAspect(self) -> Prs3d_PointAspect: ...
	def PreviousDeviationAngle(self) -> float: ...
	def PreviousDeviationCoefficient(self) -> float: ...
	def PreviousHLRDeviationAngle(self) -> float: ...
	def PreviousHLRDeviationCoefficient(self) -> float: ...
	def SectionAspect(self) -> Prs3d_LineAspect: ...
	def SeenLineAspect(self) -> Prs3d_LineAspect: ...
	def SetArrowAspect(self, theAspect: Prs3d_ArrowAspect) -> None: ...
	def SetAutoTriangulation(self, theIsEnabled: bool) -> None: ...
	def SetDatumAspect(self, theAspect: Prs3d_DatumAspect) -> None: ...
	def SetDeviationAngle(self, theAngle: float) -> None: ...
	def SetDeviationAngle(self) -> None: ...
	def SetDeviationCoefficient(self, theCoefficient: float) -> None: ...
	def SetDeviationCoefficient(self) -> None: ...
	def SetDimAngleDisplayUnits(self, theUnits: TCollection_AsciiString) -> None: ...
	def SetDimAngleModelUnits(self, theUnits: TCollection_AsciiString) -> None: ...
	def SetDimLengthDisplayUnits(self, theUnits: TCollection_AsciiString) -> None: ...
	def SetDimLengthModelUnits(self, theUnits: TCollection_AsciiString) -> None: ...
	def SetDimensionAspect(self, theAspect: Prs3d_DimensionAspect) -> None: ...
	def SetDiscretisation(self, theValue: int) -> None: ...
	def SetFaceBoundaryAspect(self, theAspect: Prs3d_LineAspect) -> None: ...
	def SetFaceBoundaryDraw(self, theIsEnabled: bool) -> None: ...
	def SetFaceBoundaryUpperContinuity(self, theMostAllowedEdgeClass: GeomAbs_Shape) -> None: ...
	def SetFreeBoundaryAspect(self, theAspect: Prs3d_LineAspect) -> None: ...
	def SetFreeBoundaryDraw(self, theIsEnabled: bool) -> None: ...
	def SetHLRAngle(self, theAngle: float) -> None: ...
	def SetHLRAngle(self) -> None: ...
	def SetHLRDeviationCoefficient(self, theCoefficient: float) -> None: ...
	def SetHLRDeviationCoefficient(self) -> None: ...
	def SetHiddenLineAspect(self, theAspect: Prs3d_LineAspect) -> None: ...
	def SetIsoOnPlane(self, theIsEnabled: bool) -> None: ...
	def SetIsoOnTriangulation(self, theToEnable: bool) -> None: ...
	def SetLineArrowDraw(self, theIsEnabled: bool) -> None: ...
	def SetLineAspect(self, theAspect: Prs3d_LineAspect) -> None: ...
	def SetLink(self, theDrawer: Prs3d_Drawer) -> None: ...
	def SetMaximalChordialDeviation(self, theChordialDeviation: float) -> None: ...
	def SetMaximalParameterValue(self, theValue: float) -> None: ...
	def SetOwnDatumAspects(self, theDefaults: Optional[Prs3d_Drawer]) -> bool: ...
	def SetOwnLineAspects(self, theDefaults: Optional[Prs3d_Drawer]) -> bool: ...
	def SetPlaneAspect(self, theAspect: Prs3d_PlaneAspect) -> None: ...
	def SetPointAspect(self, theAspect: Prs3d_PointAspect) -> None: ...
	def SetSectionAspect(self, theAspect: Prs3d_LineAspect) -> None: ...
	def SetSeenLineAspect(self, theAspect: Prs3d_LineAspect) -> None: ...
	def SetShadingAspect(self, theAspect: Prs3d_ShadingAspect) -> None: ...
	def SetTextAspect(self, theAspect: Prs3d_TextAspect) -> None: ...
	def SetTypeOfDeflection(self, theTypeOfDeflection: Aspect_TypeOfDeflection) -> None: ...
	def SetTypeOfHLR(self, theTypeOfHLR: Prs3d_TypeOfHLR) -> None: ...
	def SetUIsoAspect(self, theAspect: Prs3d_IsoAspect) -> None: ...
	def SetUnFreeBoundaryAspect(self, theAspect: Prs3d_LineAspect) -> None: ...
	def SetUnFreeBoundaryDraw(self, theIsEnabled: bool) -> None: ...
	def SetVIsoAspect(self, theAspect: Prs3d_IsoAspect) -> None: ...
	def SetVectorAspect(self, theAspect: Prs3d_LineAspect) -> None: ...
	def SetVertexDrawMode(self, theMode: Prs3d_VertexDrawMode) -> None: ...
	def SetWireAspect(self, theAspect: Prs3d_LineAspect) -> None: ...
	def SetWireDraw(self, theIsEnabled: bool) -> None: ...
	def SetupOwnFaceBoundaryAspect(self, theDefaults: Optional[Prs3d_Drawer]) -> bool: ...
	def SetupOwnPointAspect(self, theDefaults: Optional[Prs3d_Drawer]) -> bool: ...
	def SetupOwnShadingAspect(self, theDefaults: Optional[Prs3d_Drawer]) -> bool: ...
	def ShadingAspect(self) -> Prs3d_ShadingAspect: ...
	def TextAspect(self) -> Prs3d_TextAspect: ...
	def TypeOfDeflection(self) -> Aspect_TypeOfDeflection: ...
	def TypeOfHLR(self) -> Prs3d_TypeOfHLR: ...
	def UIsoAspect(self) -> Prs3d_IsoAspect: ...
	def UnFreeBoundaryAspect(self) -> Prs3d_LineAspect: ...
	def UnFreeBoundaryDraw(self) -> bool: ...
	def UnsetFaceBoundaryUpperContinuity(self) -> None: ...
	def UpdatePreviousDeviationAngle(self) -> None: ...
	def UpdatePreviousDeviationCoefficient(self) -> None: ...
	def VIsoAspect(self) -> Prs3d_IsoAspect: ...
	def VectorAspect(self) -> Prs3d_LineAspect: ...
	def VertexDrawMode(self) -> Prs3d_VertexDrawMode: ...
	def WireAspect(self) -> Prs3d_LineAspect: ...
	def WireDraw(self) -> bool: ...

class Prs3d_PresentationShadow(Graphic3d_Structure):
	def __init__(self, theViewer: Graphic3d_StructureManager, thePrs: Graphic3d_Structure) -> None: ...
	def CalculateBoundBox(self) -> None: ...
	def ParentAffinity(self) -> Graphic3d_ViewAffinity: ...
	def ParentId(self) -> int: ...

class Prs3d_Projector(Standard_Transient):
	@overload
	def __init__(self, Pr: HLRAlgo_Projector) -> None: ...
	@overload
	def __init__(self, Pers: bool, Focus: float, DX: float, DY: float, DZ: float, XAt: float, YAt: float, ZAt: float, XUp: float, YUp: float, ZUp: float) -> None: ...
	def Projector(self) -> HLRAlgo_Projector: ...

class Prs3d_Root:
	@staticmethod
	def CurrentGroup(self, thePrs3d: Prs3d_Presentation) -> Graphic3d_Group: ...
	@staticmethod
	def NewGroup(self, thePrs3d: Prs3d_Presentation) -> Graphic3d_Group: ...

class Prs3d_ShapeTool:
	def __init__(self, theShape: TopoDS_Shape, theAllVertices: Optional[bool]) -> None: ...
	def CurrentTriangulation(self, l: TopLoc_Location) -> Poly_Triangulation: ...
	def CurveBound(self) -> Bnd_Box: ...
	def FaceBound(self) -> Bnd_Box: ...
	def FacesOfEdge(self) -> TopTools_HSequenceOfShape: ...
	def GetCurve(self) -> TopoDS_Edge: ...
	def GetFace(self) -> TopoDS_Face: ...
	def GetVertex(self) -> TopoDS_Vertex: ...
	def HasCurve(self) -> bool: ...
	def HasSurface(self) -> bool: ...
	def InitCurve(self) -> None: ...
	def InitFace(self) -> None: ...
	def InitVertex(self) -> None: ...
	def IsPlanarFace(self) -> bool: ...
	@staticmethod
	def IsPlanarFace(self, theFace: TopoDS_Face) -> bool: ...
	def MoreCurve(self) -> bool: ...
	def MoreFace(self) -> bool: ...
	def MoreVertex(self) -> bool: ...
	def Neighbours(self) -> int: ...
	def NextCurve(self) -> None: ...
	def NextFace(self) -> None: ...
	def NextVertex(self) -> None: ...
	def Polygon3D(self, l: TopLoc_Location) -> Poly_Polygon3D: ...
	def PolygonOnTriangulation(self, Indices: Poly_PolygonOnTriangulation, T: Poly_Triangulation, l: TopLoc_Location) -> None: ...

class Prs3d_ToolQuadric:
	def FillArray(self, theArray: Graphic3d_ArrayOfTriangles, theTrsf: gp_Trsf) -> None: ...
	def FillArray(self, theArray: Graphic3d_ArrayOfTriangles, theTriangulation: Poly_Triangulation, theTrsf: gp_Trsf) -> None: ...
	@staticmethod
	def TrianglesNb(self, theSlicesNb: int, theStacksNb: int) -> int: ...

class Prs3d_Arrow(Prs3d_Root):
	@staticmethod
	def Draw(self, theGroup: Graphic3d_Group, theLocation: gp_Pnt, theDirection: gp_Dir, theAngle: float, theLength: float) -> None: ...
	@staticmethod
	def Draw(self, thePrs: Prs3d_Presentation, theLocation: gp_Pnt, theDirection: gp_Dir, theAngle: float, theLength: float) -> None: ...
	@staticmethod
	def DrawSegments(self, theLocation: gp_Pnt, theDir: gp_Dir, theAngle: float, theLength: float, theNbSegments: int) -> Graphic3d_ArrayOfSegments: ...
	@staticmethod
	def DrawShaded(self, theAxis: gp_Ax1, theTubeRadius: float, theAxisLength: float, theConeRadius: float, theConeLength: float, theNbFacettes: int) -> Graphic3d_ArrayOfTriangles: ...

class Prs3d_ArrowAspect(Prs3d_BasicAspect):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, anAngle: float, aLength: float) -> None: ...
	@overload
	def __init__(self, theAspect: Graphic3d_AspectLine3d) -> None: ...
	def Angle(self) -> float: ...
	def Aspect(self) -> Graphic3d_AspectLine3d: ...
	def Length(self) -> float: ...
	def SetAngle(self, anAngle: float) -> None: ...
	def SetAspect(self, theAspect: Graphic3d_AspectLine3d) -> None: ...
	def SetColor(self, theColor: Quantity_Color) -> None: ...
	def SetLength(self, theLength: float) -> None: ...

class Prs3d_DatumAspect(Prs3d_BasicAspect):
	def __init__(self) -> None: ...
	def ArrowAspect(self) -> Prs3d_ArrowAspect: ...
	def ArrowPartForAxis(self, thePart: Prs3d_DatumParts) -> Prs3d_DatumParts: ...
	def Attribute(self, theType: Prs3d_DatumAttribute) -> float: ...
	def AxisLength(self, thePart: Prs3d_DatumParts) -> float: ...
	def DatumAxes(self) -> Prs3d_DatumAxes: ...
	def DrawDatumPart(self, thePart: Prs3d_DatumParts) -> bool: ...
	def DrawFirstAndSecondAxis(self) -> bool: ...
	def DrawThirdAxis(self) -> bool: ...
	def FirstAxisAspect(self) -> Prs3d_LineAspect: ...
	def FirstAxisLength(self) -> float: ...
	def LineAspect(self, thePart: Prs3d_DatumParts) -> Prs3d_LineAspect: ...
	def PointAspect(self) -> Prs3d_PointAspect: ...
	def SecondAxisAspect(self) -> Prs3d_LineAspect: ...
	def SecondAxisLength(self) -> float: ...
	def SetArrowAspect(self, theAspect: Prs3d_ArrowAspect) -> None: ...
	def SetAttribute(self, theType: Prs3d_DatumAttribute, theValue: float) -> None: ...
	def SetAxisLength(self, theL1: float, theL2: float, theL3: float) -> None: ...
	def SetDrawArrows(self, theToDraw: bool) -> None: ...
	def SetDrawDatumAxes(self, theType: Prs3d_DatumAxes) -> None: ...
	def SetDrawFirstAndSecondAxis(self, theToDraw: bool) -> None: ...
	def SetDrawLabels(self, theToDraw: bool) -> None: ...
	def SetDrawThirdAxis(self, theToDraw: bool) -> None: ...
	def SetPointAspect(self, theAspect: Prs3d_PointAspect) -> None: ...
	def SetTextAspect(self, theTextAspect: Prs3d_TextAspect) -> None: ...
	def SetToDrawLabels(self, theToDraw: bool) -> None: ...
	def ShadingAspect(self, thePart: Prs3d_DatumParts) -> Prs3d_ShadingAspect: ...
	def TextAspect(self) -> Prs3d_TextAspect: ...
	def ThirdAxisAspect(self) -> Prs3d_LineAspect: ...
	def ThirdAxisLength(self) -> float: ...
	def ToDrawArrows(self) -> bool: ...
	def ToDrawLabels(self) -> bool: ...

class Prs3d_DimensionAspect(Prs3d_BasicAspect):
	def __init__(self) -> None: ...
	def ArrowAspect(self) -> Prs3d_ArrowAspect: ...
	def ArrowOrientation(self) -> Prs3d_DimensionArrowOrientation: ...
	def ArrowTailSize(self) -> float: ...
	def ExtensionSize(self) -> float: ...
	def IsArrows3d(self) -> bool: ...
	def IsText3d(self) -> bool: ...
	def IsTextShaded(self) -> bool: ...
	def IsUnitsDisplayed(self) -> bool: ...
	def LineAspect(self) -> Prs3d_LineAspect: ...
	def MakeArrows3d(self, theIsArrows3d: bool) -> None: ...
	def MakeText3d(self, isText3d: bool) -> None: ...
	def MakeTextShaded(self, theIsTextShaded: bool) -> None: ...
	def MakeUnitsDisplayed(self, theIsDisplayed: bool) -> None: ...
	def SetArrowAspect(self, theAspect: Prs3d_ArrowAspect) -> None: ...
	def SetArrowOrientation(self, theArrowOrient: Prs3d_DimensionArrowOrientation) -> None: ...
	def SetArrowTailSize(self, theSize: float) -> None: ...
	def SetCommonColor(self, theColor: Quantity_Color) -> None: ...
	def SetExtensionSize(self, theSize: float) -> None: ...
	def SetLineAspect(self, theAspect: Prs3d_LineAspect) -> None: ...
	def SetTextAspect(self, theAspect: Prs3d_TextAspect) -> None: ...
	def SetTextHorizontalPosition(self, thePosition: Prs3d_DimensionTextHorizontalPosition) -> None: ...
	def SetTextVerticalPosition(self, thePosition: Prs3d_DimensionTextVerticalPosition) -> None: ...
	def SetValueStringFormat(self, theFormat: TCollection_AsciiString) -> None: ...
	def TextAspect(self) -> Prs3d_TextAspect: ...
	def TextHorizontalPosition(self) -> Prs3d_DimensionTextHorizontalPosition: ...
	def TextVerticalPosition(self) -> Prs3d_DimensionTextVerticalPosition: ...
	def ValueStringFormat(self) -> TCollection_AsciiString: ...

class Prs3d_LineAspect(Prs3d_BasicAspect):
	@overload
	def __init__(self, theColor: Quantity_Color, theType: Aspect_TypeOfLine, theWidth: float) -> None: ...
	@overload
	def __init__(self, theAspect: Graphic3d_AspectLine3d) -> None: ...
	def Aspect(self) -> Graphic3d_AspectLine3d: ...
	def SetAspect(self, theAspect: Graphic3d_AspectLine3d) -> None: ...
	def SetColor(self, theColor: Quantity_Color) -> None: ...
	def SetTypeOfLine(self, theType: Aspect_TypeOfLine) -> None: ...
	def SetWidth(self, theWidth: float) -> None: ...

class Prs3d_PlaneAspect(Prs3d_BasicAspect):
	def __init__(self) -> None: ...
	def ArrowAspect(self) -> Prs3d_LineAspect: ...
	def ArrowsAngle(self) -> float: ...
	def ArrowsLength(self) -> float: ...
	def ArrowsSize(self) -> float: ...
	def DisplayCenterArrow(self) -> bool: ...
	def DisplayEdges(self) -> bool: ...
	def DisplayEdgesArrows(self) -> bool: ...
	def DisplayIso(self) -> bool: ...
	def EdgesAspect(self) -> Prs3d_LineAspect: ...
	def IsoAspect(self) -> Prs3d_LineAspect: ...
	def IsoDistance(self) -> float: ...
	def PlaneXLength(self) -> float: ...
	def PlaneYLength(self) -> float: ...
	def SetArrowsAngle(self, theAngle: float) -> None: ...
	def SetArrowsLength(self, theLength: float) -> None: ...
	def SetArrowsSize(self, theSize: float) -> None: ...
	def SetDisplayCenterArrow(self, theToDraw: bool) -> None: ...
	def SetDisplayEdges(self, theToDraw: bool) -> None: ...
	def SetDisplayEdgesArrows(self, theToDraw: bool) -> None: ...
	def SetDisplayIso(self, theToDraw: bool) -> None: ...
	def SetIsoDistance(self, theL: float) -> None: ...
	def SetPlaneLength(self, theLX: float, theLY: float) -> None: ...

class Prs3d_PointAspect(Prs3d_BasicAspect):
	@overload
	def __init__(self, theType: Aspect_TypeOfMarker, theColor: Quantity_Color, theScale: float) -> None: ...
	@overload
	def __init__(self, theColor: Quantity_Color, theWidth: int, theHeight: int, theTexture: TColStd_HArray1OfByte) -> None: ...
	@overload
	def __init__(self, theAspect: Graphic3d_AspectMarker3d) -> None: ...
	def Aspect(self) -> Graphic3d_AspectMarker3d: ...
	def GetTexture(self) -> Graphic3d_MarkerImage: ...
	def GetTextureSize(self) -> Tuple[int, int]: ...
	def SetAspect(self, theAspect: Graphic3d_AspectMarker3d) -> None: ...
	def SetColor(self, theColor: Quantity_Color) -> None: ...
	def SetScale(self, theScale: float) -> None: ...
	def SetTypeOfMarker(self, theType: Aspect_TypeOfMarker) -> None: ...

class Prs3d_ShadingAspect(Prs3d_BasicAspect):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAspect: Graphic3d_AspectFillArea3d) -> None: ...
	def Aspect(self) -> Graphic3d_AspectFillArea3d: ...
	def Color(self, aModel: Optional[Aspect_TypeOfFacingModel]) -> Quantity_Color: ...
	def Material(self, aModel: Optional[Aspect_TypeOfFacingModel]) -> Graphic3d_MaterialAspect: ...
	def SetAspect(self, theAspect: Graphic3d_AspectFillArea3d) -> None: ...
	def SetColor(self, aColor: Quantity_Color, aModel: Optional[Aspect_TypeOfFacingModel]) -> None: ...
	def SetMaterial(self, aMaterial: Graphic3d_MaterialAspect, aModel: Optional[Aspect_TypeOfFacingModel]) -> None: ...
	def SetTransparency(self, aValue: float, aModel: Optional[Aspect_TypeOfFacingModel]) -> None: ...
	def Transparency(self, aModel: Optional[Aspect_TypeOfFacingModel]) -> float: ...

class Prs3d_Text(Prs3d_Root):
	@staticmethod
	def Draw(self, theGroup: Graphic3d_Group, theAspect: Prs3d_TextAspect, theText: TCollection_ExtendedString, theAttachmentPoint: gp_Pnt) -> None: ...
	@staticmethod
	def Draw(self, theGroup: Graphic3d_Group, theAspect: Prs3d_TextAspect, theText: TCollection_ExtendedString, theOrientation: gp_Ax2, theHasOwnAnchor: Optional[bool]) -> None: ...
	@staticmethod
	def Draw(self, thePrs: Prs3d_Presentation, theDrawer: Prs3d_Drawer, theText: TCollection_ExtendedString, theAttachmentPoint: gp_Pnt) -> None: ...
	@staticmethod
	def Draw(self, thePrs: Prs3d_Presentation, theAspect: Prs3d_TextAspect, theText: TCollection_ExtendedString, theOrientation: gp_Ax2, theHasOwnAnchor: Optional[bool]) -> None: ...
	@staticmethod
	def Draw(self, thePrs: Prs3d_Presentation, theAspect: Prs3d_TextAspect, theText: TCollection_ExtendedString, theAttachmentPoint: gp_Pnt) -> None: ...

class Prs3d_TextAspect(Prs3d_BasicAspect):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theAspect: Graphic3d_AspectText3d) -> None: ...
	def Angle(self) -> float: ...
	def Aspect(self) -> Graphic3d_AspectText3d: ...
	def Height(self) -> float: ...
	def HorizontalJustification(self) -> Graphic3d_HorizontalTextAlignment: ...
	def Orientation(self) -> Graphic3d_TextPath: ...
	def SetAngle(self, theAngle: float) -> None: ...
	def SetAspect(self, theAspect: Graphic3d_AspectText3d) -> None: ...
	def SetColor(self, theColor: Quantity_Color) -> None: ...
	def SetFont(self, theFont: str) -> None: ...
	def SetHeight(self, theHeight: float) -> None: ...
	def SetHorizontalJustification(self, theJustification: Graphic3d_HorizontalTextAlignment) -> None: ...
	def SetOrientation(self, theOrientation: Graphic3d_TextPath) -> None: ...
	def SetVerticalJustification(self, theJustification: Graphic3d_VerticalTextAlignment) -> None: ...
	def VerticalJustification(self) -> Graphic3d_VerticalTextAlignment: ...

class Prs3d_ToolCylinder(Prs3d_ToolQuadric):
	def __init__(self, theBottomRad: float, theTopRad: float, theHeight: float, theNbSlices: int, theNbStacks: int) -> None: ...
	@staticmethod
	def Create(self, theBottomRad: float, theTopRad: float, theHeight: float, theNbSlices: int, theNbStacks: int, theTrsf: gp_Trsf) -> Graphic3d_ArrayOfTriangles: ...

class Prs3d_ToolDisk(Prs3d_ToolQuadric):
	def __init__(self, theInnerRadius: float, theOuterRadius: float, theNbSlices: int, theNbStacks: int) -> None: ...
	@staticmethod
	def Create(self, theInnerRadius: float, theOuterRadius: float, theNbSlices: int, theNbStacks: int, theTrsf: gp_Trsf) -> Graphic3d_ArrayOfTriangles: ...
	def SetAngleRange(self, theStartAngle: float, theEndAngle: float) -> None: ...

class Prs3d_ToolSector(Prs3d_ToolQuadric):
	def __init__(self, theRadius: float, theNbSlices: int, theNbStacks: int) -> None: ...
	@staticmethod
	def Create(self, theRadius: float, theNbSlices: int, theNbStacks: int, theTrsf: gp_Trsf) -> Graphic3d_ArrayOfTriangles: ...

class Prs3d_ToolSphere(Prs3d_ToolQuadric):
	def __init__(self, theRadius: float, theNbSlices: int, theNbStacks: int) -> None: ...
	@staticmethod
	def Create(self, theRadius: float, theNbSlices: int, theNbStacks: int, theTrsf: gp_Trsf) -> Graphic3d_ArrayOfTriangles: ...

class Prs3d_IsoAspect(Prs3d_LineAspect):
	def __init__(self, theColor: Quantity_Color, theType: Aspect_TypeOfLine, theWidth: float, theNumber: int) -> None: ...
	def Number(self) -> int: ...
	def SetNumber(self, theNumber: int) -> None: ...
