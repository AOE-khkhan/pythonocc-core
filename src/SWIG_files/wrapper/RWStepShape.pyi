from typing import overload, NewType, Optional, Tuple

from OCC.Core.RWStepShape import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.StepData import *
from OCC.Core.Interface import *
from OCC.Core.StepShape import *


class RWStepShape_RWAdvancedBrepShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_AdvancedBrepShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_AdvancedBrepShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_AdvancedBrepShapeRepresentation) -> None: ...

class RWStepShape_RWAdvancedFace:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_AdvancedFace) -> None: ...
	def Share(self, ent: StepShape_AdvancedFace, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_AdvancedFace) -> None: ...

class RWStepShape_RWAngularLocation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_AngularLocation) -> None: ...
	def Share(self, ent: StepShape_AngularLocation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_AngularLocation) -> None: ...

class RWStepShape_RWAngularSize:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_AngularSize) -> None: ...
	def Share(self, ent: StepShape_AngularSize, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_AngularSize) -> None: ...

class RWStepShape_RWBlock:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_Block) -> None: ...
	def Share(self, ent: StepShape_Block, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_Block) -> None: ...

class RWStepShape_RWBooleanResult:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_BooleanResult) -> None: ...
	def Share(self, ent: StepShape_BooleanResult, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_BooleanResult) -> None: ...

class RWStepShape_RWBoxDomain:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_BoxDomain) -> None: ...
	def Share(self, ent: StepShape_BoxDomain, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_BoxDomain) -> None: ...

class RWStepShape_RWBoxedHalfSpace:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_BoxedHalfSpace) -> None: ...
	def Share(self, ent: StepShape_BoxedHalfSpace, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_BoxedHalfSpace) -> None: ...

class RWStepShape_RWBrepWithVoids:
	def __init__(self) -> None: ...
	def Check(self, ent: StepShape_BrepWithVoids, shares: Interface_ShareTool, ach: Interface_Check) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_BrepWithVoids) -> None: ...
	def Share(self, ent: StepShape_BrepWithVoids, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_BrepWithVoids) -> None: ...

class RWStepShape_RWClosedShell:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ClosedShell) -> None: ...
	def Share(self, ent: StepShape_ClosedShell, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ClosedShell) -> None: ...

class RWStepShape_RWCompoundShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_CompoundShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_CompoundShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_CompoundShapeRepresentation) -> None: ...

class RWStepShape_RWConnectedEdgeSet:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ConnectedEdgeSet) -> None: ...
	def Share(self, ent: StepShape_ConnectedEdgeSet, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ConnectedEdgeSet) -> None: ...

class RWStepShape_RWConnectedFaceSet:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ConnectedFaceSet) -> None: ...
	def Share(self, ent: StepShape_ConnectedFaceSet, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ConnectedFaceSet) -> None: ...

class RWStepShape_RWConnectedFaceShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ConnectedFaceShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_ConnectedFaceShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ConnectedFaceShapeRepresentation) -> None: ...

class RWStepShape_RWConnectedFaceSubSet:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ConnectedFaceSubSet) -> None: ...
	def Share(self, ent: StepShape_ConnectedFaceSubSet, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ConnectedFaceSubSet) -> None: ...

class RWStepShape_RWContextDependentShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ContextDependentShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_ContextDependentShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ContextDependentShapeRepresentation) -> None: ...

class RWStepShape_RWCsgShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_CsgShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_CsgShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_CsgShapeRepresentation) -> None: ...

class RWStepShape_RWCsgSolid:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_CsgSolid) -> None: ...
	def Share(self, ent: StepShape_CsgSolid, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_CsgSolid) -> None: ...

class RWStepShape_RWDefinitionalRepresentationAndShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_DefinitionalRepresentationAndShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_DefinitionalRepresentationAndShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_DefinitionalRepresentationAndShapeRepresentation) -> None: ...

class RWStepShape_RWDimensionalCharacteristicRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_DimensionalCharacteristicRepresentation) -> None: ...
	def Share(self, ent: StepShape_DimensionalCharacteristicRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_DimensionalCharacteristicRepresentation) -> None: ...

class RWStepShape_RWDimensionalLocation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_DimensionalLocation) -> None: ...
	def Share(self, ent: StepShape_DimensionalLocation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_DimensionalLocation) -> None: ...

class RWStepShape_RWDimensionalLocationWithPath:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_DimensionalLocationWithPath) -> None: ...
	def Share(self, ent: StepShape_DimensionalLocationWithPath, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_DimensionalLocationWithPath) -> None: ...

class RWStepShape_RWDimensionalSize:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_DimensionalSize) -> None: ...
	def Share(self, ent: StepShape_DimensionalSize, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_DimensionalSize) -> None: ...

class RWStepShape_RWDimensionalSizeWithPath:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_DimensionalSizeWithPath) -> None: ...
	def Share(self, ent: StepShape_DimensionalSizeWithPath, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_DimensionalSizeWithPath) -> None: ...

class RWStepShape_RWEdge:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_Edge) -> None: ...
	def Share(self, ent: StepShape_Edge, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_Edge) -> None: ...

class RWStepShape_RWEdgeBasedWireframeModel:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_EdgeBasedWireframeModel) -> None: ...
	def Share(self, ent: StepShape_EdgeBasedWireframeModel, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_EdgeBasedWireframeModel) -> None: ...

class RWStepShape_RWEdgeBasedWireframeShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_EdgeBasedWireframeShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_EdgeBasedWireframeShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_EdgeBasedWireframeShapeRepresentation) -> None: ...

class RWStepShape_RWEdgeCurve:
	def __init__(self) -> None: ...
	def Check(self, ent: StepShape_EdgeCurve, shares: Interface_ShareTool, ach: Interface_Check) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_EdgeCurve) -> None: ...
	def Share(self, ent: StepShape_EdgeCurve, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_EdgeCurve) -> None: ...

class RWStepShape_RWEdgeLoop:
	def __init__(self) -> None: ...
	def Check(self, ent: StepShape_EdgeLoop, shares: Interface_ShareTool, ach: Interface_Check) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_EdgeLoop) -> None: ...
	def Share(self, ent: StepShape_EdgeLoop, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_EdgeLoop) -> None: ...

class RWStepShape_RWExtrudedAreaSolid:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ExtrudedAreaSolid) -> None: ...
	def Share(self, ent: StepShape_ExtrudedAreaSolid, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ExtrudedAreaSolid) -> None: ...

class RWStepShape_RWExtrudedFaceSolid:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ExtrudedFaceSolid) -> None: ...
	def Share(self, ent: StepShape_ExtrudedFaceSolid, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ExtrudedFaceSolid) -> None: ...

class RWStepShape_RWFace:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_Face) -> None: ...
	def Share(self, ent: StepShape_Face, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_Face) -> None: ...

class RWStepShape_RWFaceBasedSurfaceModel:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_FaceBasedSurfaceModel) -> None: ...
	def Share(self, ent: StepShape_FaceBasedSurfaceModel, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_FaceBasedSurfaceModel) -> None: ...

class RWStepShape_RWFaceBound:
	def __init__(self) -> None: ...
	def Check(self, ent: StepShape_FaceBound, shares: Interface_ShareTool, ach: Interface_Check) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_FaceBound) -> None: ...
	def Share(self, ent: StepShape_FaceBound, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_FaceBound) -> None: ...

class RWStepShape_RWFaceOuterBound:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_FaceOuterBound) -> None: ...
	def Share(self, ent: StepShape_FaceOuterBound, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_FaceOuterBound) -> None: ...

class RWStepShape_RWFaceSurface:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_FaceSurface) -> None: ...
	def Share(self, ent: StepShape_FaceSurface, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_FaceSurface) -> None: ...

class RWStepShape_RWFacetedBrep:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_FacetedBrep) -> None: ...
	def Share(self, ent: StepShape_FacetedBrep, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_FacetedBrep) -> None: ...

class RWStepShape_RWFacetedBrepAndBrepWithVoids:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_FacetedBrepAndBrepWithVoids) -> None: ...
	def Share(self, ent: StepShape_FacetedBrepAndBrepWithVoids, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_FacetedBrepAndBrepWithVoids) -> None: ...

class RWStepShape_RWFacetedBrepShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_FacetedBrepShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_FacetedBrepShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_FacetedBrepShapeRepresentation) -> None: ...

class RWStepShape_RWGeometricCurveSet:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_GeometricCurveSet) -> None: ...
	def Share(self, ent: StepShape_GeometricCurveSet, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_GeometricCurveSet) -> None: ...

class RWStepShape_RWGeometricSet:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_GeometricSet) -> None: ...
	def Share(self, ent: StepShape_GeometricSet, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_GeometricSet) -> None: ...

class RWStepShape_RWGeometricallyBoundedSurfaceShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_GeometricallyBoundedSurfaceShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_GeometricallyBoundedSurfaceShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_GeometricallyBoundedSurfaceShapeRepresentation) -> None: ...

class RWStepShape_RWGeometricallyBoundedWireframeShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_GeometricallyBoundedWireframeShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_GeometricallyBoundedWireframeShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_GeometricallyBoundedWireframeShapeRepresentation) -> None: ...

class RWStepShape_RWHalfSpaceSolid:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_HalfSpaceSolid) -> None: ...
	def Share(self, ent: StepShape_HalfSpaceSolid, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_HalfSpaceSolid) -> None: ...

class RWStepShape_RWLimitsAndFits:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_LimitsAndFits) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_LimitsAndFits) -> None: ...

class RWStepShape_RWLoop:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_Loop) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_Loop) -> None: ...

class RWStepShape_RWLoopAndPath:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_LoopAndPath) -> None: ...
	def Share(self, ent: StepShape_LoopAndPath, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_LoopAndPath) -> None: ...

class RWStepShape_RWManifoldSolidBrep:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ManifoldSolidBrep) -> None: ...
	def Share(self, ent: StepShape_ManifoldSolidBrep, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ManifoldSolidBrep) -> None: ...

class RWStepShape_RWManifoldSurfaceShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ManifoldSurfaceShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_ManifoldSurfaceShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ManifoldSurfaceShapeRepresentation) -> None: ...

class RWStepShape_RWMeasureQualification:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_MeasureQualification) -> None: ...
	def Share(self, ent: StepShape_MeasureQualification, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_MeasureQualification) -> None: ...

class RWStepShape_RWMeasureRepresentationItemAndQualifiedRepresentationItem:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_MeasureRepresentationItemAndQualifiedRepresentationItem) -> None: ...
	def Share(self, ent: StepShape_MeasureRepresentationItemAndQualifiedRepresentationItem, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_MeasureRepresentationItemAndQualifiedRepresentationItem) -> None: ...

class RWStepShape_RWNonManifoldSurfaceShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_NonManifoldSurfaceShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_NonManifoldSurfaceShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_NonManifoldSurfaceShapeRepresentation) -> None: ...

class RWStepShape_RWOpenShell:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_OpenShell) -> None: ...
	def Share(self, ent: StepShape_OpenShell, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_OpenShell) -> None: ...

class RWStepShape_RWOrientedClosedShell:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_OrientedClosedShell) -> None: ...
	def Share(self, ent: StepShape_OrientedClosedShell, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_OrientedClosedShell) -> None: ...

class RWStepShape_RWOrientedEdge:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_OrientedEdge) -> None: ...
	def Share(self, ent: StepShape_OrientedEdge, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_OrientedEdge) -> None: ...

class RWStepShape_RWOrientedFace:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_OrientedFace) -> None: ...
	def Share(self, ent: StepShape_OrientedFace, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_OrientedFace) -> None: ...

class RWStepShape_RWOrientedOpenShell:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_OrientedOpenShell) -> None: ...
	def Share(self, ent: StepShape_OrientedOpenShell, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_OrientedOpenShell) -> None: ...

class RWStepShape_RWOrientedPath:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_OrientedPath) -> None: ...
	def Share(self, ent: StepShape_OrientedPath, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_OrientedPath) -> None: ...

class RWStepShape_RWPath:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_Path) -> None: ...
	def Share(self, ent: StepShape_Path, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_Path) -> None: ...

class RWStepShape_RWPlusMinusTolerance:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_PlusMinusTolerance) -> None: ...
	def Share(self, ent: StepShape_PlusMinusTolerance, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_PlusMinusTolerance) -> None: ...

class RWStepShape_RWPointRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_PointRepresentation) -> None: ...
	def Share(self, ent: StepShape_PointRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_PointRepresentation) -> None: ...

class RWStepShape_RWPolyLoop:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_PolyLoop) -> None: ...
	def Share(self, ent: StepShape_PolyLoop, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_PolyLoop) -> None: ...

class RWStepShape_RWPrecisionQualifier:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_PrecisionQualifier) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_PrecisionQualifier) -> None: ...

class RWStepShape_RWQualifiedRepresentationItem:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_QualifiedRepresentationItem) -> None: ...
	def Share(self, ent: StepShape_QualifiedRepresentationItem, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_QualifiedRepresentationItem) -> None: ...

class RWStepShape_RWRevolvedAreaSolid:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_RevolvedAreaSolid) -> None: ...
	def Share(self, ent: StepShape_RevolvedAreaSolid, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_RevolvedAreaSolid) -> None: ...

class RWStepShape_RWRevolvedFaceSolid:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_RevolvedFaceSolid) -> None: ...
	def Share(self, ent: StepShape_RevolvedFaceSolid, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_RevolvedFaceSolid) -> None: ...

class RWStepShape_RWRightAngularWedge:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_RightAngularWedge) -> None: ...
	def Share(self, ent: StepShape_RightAngularWedge, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_RightAngularWedge) -> None: ...

class RWStepShape_RWRightCircularCone:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_RightCircularCone) -> None: ...
	def Share(self, ent: StepShape_RightCircularCone, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_RightCircularCone) -> None: ...

class RWStepShape_RWRightCircularCylinder:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_RightCircularCylinder) -> None: ...
	def Share(self, ent: StepShape_RightCircularCylinder, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_RightCircularCylinder) -> None: ...

class RWStepShape_RWSeamEdge:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_SeamEdge) -> None: ...
	def Share(self, ent: StepShape_SeamEdge, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_SeamEdge) -> None: ...

class RWStepShape_RWShapeDefinitionRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ShapeDefinitionRepresentation) -> None: ...
	def Share(self, ent: StepShape_ShapeDefinitionRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ShapeDefinitionRepresentation) -> None: ...

class RWStepShape_RWShapeDimensionRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ShapeDimensionRepresentation) -> None: ...
	def Share(self, ent: StepShape_ShapeDimensionRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ShapeDimensionRepresentation) -> None: ...

class RWStepShape_RWShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_ShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ShapeRepresentation) -> None: ...

class RWStepShape_RWShapeRepresentationWithParameters:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ShapeRepresentationWithParameters) -> None: ...
	def Share(self, ent: StepShape_ShapeRepresentationWithParameters, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ShapeRepresentationWithParameters) -> None: ...

class RWStepShape_RWShellBasedSurfaceModel:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ShellBasedSurfaceModel) -> None: ...
	def Share(self, ent: StepShape_ShellBasedSurfaceModel, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ShellBasedSurfaceModel) -> None: ...

class RWStepShape_RWSolidModel:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_SolidModel) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_SolidModel) -> None: ...

class RWStepShape_RWSolidReplica:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_SolidReplica) -> None: ...
	def Share(self, ent: StepShape_SolidReplica, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_SolidReplica) -> None: ...

class RWStepShape_RWSphere:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_Sphere) -> None: ...
	def Share(self, ent: StepShape_Sphere, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_Sphere) -> None: ...

class RWStepShape_RWSubedge:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_Subedge) -> None: ...
	def Share(self, ent: StepShape_Subedge, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_Subedge) -> None: ...

class RWStepShape_RWSubface:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_Subface) -> None: ...
	def Share(self, ent: StepShape_Subface, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_Subface) -> None: ...

class RWStepShape_RWSweptAreaSolid:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_SweptAreaSolid) -> None: ...
	def Share(self, ent: StepShape_SweptAreaSolid, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_SweptAreaSolid) -> None: ...

class RWStepShape_RWSweptFaceSolid:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_SweptFaceSolid) -> None: ...
	def Share(self, ent: StepShape_SweptFaceSolid, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_SweptFaceSolid) -> None: ...

class RWStepShape_RWToleranceValue:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ToleranceValue) -> None: ...
	def Share(self, ent: StepShape_ToleranceValue, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ToleranceValue) -> None: ...

class RWStepShape_RWTopologicalRepresentationItem:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_TopologicalRepresentationItem) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_TopologicalRepresentationItem) -> None: ...

class RWStepShape_RWTorus:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_Torus) -> None: ...
	def Share(self, ent: StepShape_Torus, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_Torus) -> None: ...

class RWStepShape_RWTransitionalShapeRepresentation:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_TransitionalShapeRepresentation) -> None: ...
	def Share(self, ent: StepShape_TransitionalShapeRepresentation, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_TransitionalShapeRepresentation) -> None: ...

class RWStepShape_RWTypeQualifier:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_TypeQualifier) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_TypeQualifier) -> None: ...

class RWStepShape_RWValueFormatTypeQualifier:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_ValueFormatTypeQualifier) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_ValueFormatTypeQualifier) -> None: ...

class RWStepShape_RWVertex:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_Vertex) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_Vertex) -> None: ...

class RWStepShape_RWVertexLoop:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_VertexLoop) -> None: ...
	def Share(self, ent: StepShape_VertexLoop, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_VertexLoop) -> None: ...

class RWStepShape_RWVertexPoint:
	def __init__(self) -> None: ...
	def ReadStep(self, data: StepData_StepReaderData, num: int, ach: Interface_Check, ent: StepShape_VertexPoint) -> None: ...
	def Share(self, ent: StepShape_VertexPoint, iter: Interface_EntityIterator) -> None: ...
	def WriteStep(self, SW: StepData_StepWriter, ent: StepShape_VertexPoint) -> None: ...
