import importlib
from typing import TYPE_CHECKING

import pytest

from qtpy import API_NAME, PYQT6, PYSIDE6

if TYPE_CHECKING:
    from types import ModuleType


@pytest.mark.skipif(PYQT6, reason="Not complete in PyQt6")
@pytest.mark.skipif(PYSIDE6, reason="Not complete in PySide6")
def test_qt3drender():
    """Test the qtpy.Qt3DRender namespace"""
    Qt3DRender = pytest.importorskip("qtpy.Qt3DRender")

    assert Qt3DRender.QPointSize is not None
    assert Qt3DRender.QFrustumCulling is not None
    assert Qt3DRender.QPickPointEvent is not None
    assert Qt3DRender.QRenderPassFilter is not None
    assert Qt3DRender.QMesh is not None
    assert Qt3DRender.QRayCaster is not None
    assert Qt3DRender.QStencilMask is not None
    assert Qt3DRender.QPickLineEvent is not None
    assert Qt3DRender.QPickTriangleEvent is not None
    assert Qt3DRender.QRenderState is not None
    assert Qt3DRender.QTextureWrapMode is not None
    assert Qt3DRender.QRenderPass is not None
    assert Qt3DRender.QGeometryRenderer is not None
    assert Qt3DRender.QAttribute is not None
    assert Qt3DRender.QStencilOperation is not None
    assert Qt3DRender.QScissorTest is not None
    assert Qt3DRender.QTextureCubeMapArray is not None
    assert Qt3DRender.QRenderTarget is not None
    assert Qt3DRender.QStencilTest is not None
    assert Qt3DRender.QTextureData is not None
    assert Qt3DRender.QBuffer is not None
    assert Qt3DRender.QLineWidth is not None
    assert Qt3DRender.QLayer is not None
    assert Qt3DRender.QTextureRectangle is not None
    assert Qt3DRender.QRenderTargetSelector is not None
    assert Qt3DRender.QPickingSettings is not None
    assert Qt3DRender.QCullFace is not None
    assert Qt3DRender.QAbstractFunctor is not None
    assert Qt3DRender.PropertyReaderInterface is not None
    assert Qt3DRender.QMaterial is not None
    assert Qt3DRender.QAlphaCoverage is not None
    assert Qt3DRender.QClearBuffers is not None
    assert Qt3DRender.QAlphaTest is not None
    assert Qt3DRender.QStencilOperationArguments is not None
    assert Qt3DRender.QTexture2DMultisample is not None
    assert Qt3DRender.QLevelOfDetailSwitch is not None
    assert Qt3DRender.QRenderStateSet is not None
    assert Qt3DRender.QViewport is not None
    assert Qt3DRender.QObjectPicker is not None
    assert Qt3DRender.QPolygonOffset is not None
    assert Qt3DRender.QRenderSettings is not None
    assert Qt3DRender.QFrontFace is not None
    assert Qt3DRender.QTexture3D is not None
    assert Qt3DRender.QTextureBuffer is not None
    assert Qt3DRender.QTechniqueFilter is not None
    assert Qt3DRender.QLayerFilter is not None
    assert Qt3DRender.QFilterKey is not None
    assert Qt3DRender.QRenderSurfaceSelector is not None
    assert Qt3DRender.QEnvironmentLight is not None
    assert Qt3DRender.QMemoryBarrier is not None
    assert Qt3DRender.QNoDepthMask is not None
    assert Qt3DRender.QBlitFramebuffer is not None
    assert Qt3DRender.QGraphicsApiFilter is not None
    assert Qt3DRender.QAbstractTexture is not None
    assert Qt3DRender.QRenderCaptureReply is not None
    assert Qt3DRender.QAbstractLight is not None
    assert Qt3DRender.QAbstractRayCaster is not None
    assert Qt3DRender.QDirectionalLight is not None
    assert Qt3DRender.QDispatchCompute is not None
    assert Qt3DRender.QBufferDataGenerator is not None
    assert Qt3DRender.QPointLight is not None
    assert Qt3DRender.QStencilTestArguments is not None
    assert Qt3DRender.QTexture1D is not None
    assert Qt3DRender.QCameraSelector is not None
    assert Qt3DRender.QProximityFilter is not None
    assert Qt3DRender.QTexture1DArray is not None
    assert Qt3DRender.QBlendEquation is not None
    assert Qt3DRender.QTextureImageDataGenerator is not None
    assert Qt3DRender.QSpotLight is not None
    assert Qt3DRender.QEffect is not None
    assert Qt3DRender.QSeamlessCubemap is not None
    assert Qt3DRender.QTexture2DMultisampleArray is not None
    assert Qt3DRender.QComputeCommand is not None
    assert Qt3DRender.QFrameGraphNode is not None
    assert Qt3DRender.QSortPolicy is not None
    assert Qt3DRender.QTextureImageData is not None
    assert Qt3DRender.QCamera is not None
    assert Qt3DRender.QGeometry is not None
    assert Qt3DRender.QScreenRayCaster is not None
    assert Qt3DRender.QClipPlane is not None
    assert Qt3DRender.QMultiSampleAntiAliasing is not None
    assert Qt3DRender.QRayCasterHit is not None
    assert Qt3DRender.QAbstractTextureImage is not None
    assert Qt3DRender.QNoDraw is not None
    assert Qt3DRender.QPickEvent is not None
    assert Qt3DRender.QRenderCapture is not None
    assert Qt3DRender.QDepthTest is not None
    assert Qt3DRender.QParameter is not None
    assert Qt3DRender.QLevelOfDetail is not None
    assert Qt3DRender.QGeometryFactory is not None
    assert Qt3DRender.QTexture2D is not None
    assert Qt3DRender.QRenderAspect is not None
    assert Qt3DRender.QPaintedTextureImage is not None
    assert Qt3DRender.QDithering is not None
    assert Qt3DRender.QTextureGenerator is not None
    assert Qt3DRender.QBlendEquationArguments is not None
    assert Qt3DRender.QLevelOfDetailBoundingSphere is not None
    assert Qt3DRender.QColorMask is not None
    assert Qt3DRender.QSceneLoader is not None
    assert Qt3DRender.QTextureLoader is not None
    assert Qt3DRender.QShaderProgram is not None
    assert Qt3DRender.QTextureCubeMap is not None
    assert Qt3DRender.QTexture2DArray is not None
    assert Qt3DRender.QTextureImage is not None
    assert Qt3DRender.QCameraLens is not None
    assert Qt3DRender.QRenderTargetOutput is not None
    assert Qt3DRender.QShaderProgramBuilder is not None
    assert Qt3DRender.QTechnique is not None
    assert Qt3DRender.QShaderData is not None


@pytest.mark.skipif(PYQT6, reason="Not complete in PyQt6")
@pytest.mark.skipif(PYSIDE6, reason="Not complete in PySide6")
def test_namespace_not_polluted():
    """Test that no extra members are exported into the module namespace."""
    qtpy_module: ModuleType = pytest.importorskip("qtpy.Qt3DRender")
    original_module: ModuleType = importlib.import_module(
        qtpy_module.__name__.replace("qtpy", API_NAME),
    )

    extra_members = (
        frozenset(object.__dir__(qtpy_module))
        - frozenset(dir(original_module))
        - frozenset(
            # These are unavoidable:
            [
                "__builtins__",
                "__cached__",
            ],
        )
        - frozenset(
            # These don't show up in `dir()` when on PySide:
            [*dir(object), "PropertyReaderInterface", "QAbstractFunctor", "QAbstractLight", "QAbstractRayCaster", "QAbstractTexture", "QAbstractTextureImage", "QAlphaCoverage", "QAlphaTest", "QAttribute", "QBlendEquation", "QBlendEquationArguments", "QBlitFramebuffer", "QBuffer", "QBufferCapture", "QBufferDataGenerator", "QCamera", "QCameraLens", "QCameraSelector", "QClearBuffers", "QClipPlane", "QColorMask", "QComputeCommand", "QCullFace", "QDepthTest", "QDirectionalLight", "QDispatchCompute", "QDithering", "QEffect", "QEnvironmentLight", "QFilterKey", "QFrameGraphNode", "QFrameGraphNodeCreatedChangeBase", "QFrontFace", "QFrustumCulling", "QGeometry", "QGeometryFactory", "QGeometryRenderer", "QGraphicsApiFilter", "QLayer", "QLayerFilter", "QLevelOfDetail", "QLevelOfDetailBoundingSphere", "QLevelOfDetailSwitch", "QLineWidth", "QMaterial", "QMemoryBarrier", "QMesh", "QMultiSampleAntiAliasing", "QNoDepthMask", "QNoDraw", "QObjectPicker", "QPaintedTextureImage", "QParameter", "QPickEvent", "QPickLineEvent", "QPickPointEvent", "QPickTriangleEvent", "QPickingSettings", "QPointLight", "QPointSize", "QPolygonOffset", "QProximityFilter", "QRayCaster", "QRayCasterHit", "QRenderAspect", "QRenderCapture", "QRenderCaptureReply", "QRenderPass", "QRenderPassFilter", "QRenderSettings", "QRenderState", "QRenderStateSet", "QRenderSurfaceSelector", "QRenderTarget", "QRenderTargetOutput", "QRenderTargetSelector", "QSceneLoader", "QScissorTest", "QScreenRayCaster", "QSeamlessCubemap", "QSetFence", "QShaderData", "QShaderProgram", "QShaderProgramBuilder", "QSharedGLTexture", "QSortPolicy", "QSpotLight", "QStencilMask", "QStencilOperation", "QStencilOperationArguments", "QStencilTest", "QStencilTestArguments", "QTechnique", "QTechniqueFilter", "QTexture1D", "QTexture1DArray", "QTexture2D", "QTexture2DArray", "QTexture2DMultisample", "QTexture2DMultisampleArray", "QTexture3D", "QTextureBuffer", "QTextureCubeMap", "QTextureCubeMapArray", "QTextureData", "QTextureGenerator", "QTextureImage", "QTextureImageData", "QTextureImageDataGenerator", "QTextureLoader", "QTextureRectangle", "QTextureWrapMode", "QViewport", "QWaitFence", "__annotations__", "__dict__", "__module__"],
        )
    )
    assert not extra_members
