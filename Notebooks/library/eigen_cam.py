from base_cam import BaseCAM
from svd_on_activations import get_2d_projection

# https://ieeexplore.ieee.org/abstract/document/9206626?casa_token=C3Jx-YJBreEAAAAA:Ur6fHgDtIoKjLLhqnSpN3RETlFI3eTao1lAYmXUJYg3uLrKqW4PTq5ZtmiA5pTUeRKUpvtHLWIA

class EigenCAM(BaseCAM):
    def __init__(self, model, target_layers, use_cuda=False,
                 reshape_transform=None):
        super(EigenCAM, self).__init__(model,
                                       target_layers,
                                       use_cuda,
                                       reshape_transform,
                                       uses_gradients=False)

    def get_cam_image(self,
                      input_tensor,
                      target_layer,
                      target_category,
                      activations,
                      grads,
                      eigen_smooth):
        return get_2d_projection(activations)

# Eigen Grad-CAM
# Like Eigen CAM: https://ieeexplore.ieee.org/abstract/document/9206626?casa_token=90r8u-85v88AAAAA:eER_sDGMzkRdhPF2jaAt0pNWIYKpyG-nqG2QRRkiOPG9g0QRMVhq9S2hpsU6QvdoDq_KqrZnBoE
# But multiply the activations x gradients

class EigenGradCAM(BaseCAM):
    def __init__(self, model, target_layers, use_cuda=False,
                 reshape_transform=None):
        super(EigenGradCAM, self).__init__(model, target_layers, use_cuda,
                                           reshape_transform)

    def get_cam_image(self,
                      input_tensor,
                      target_layer,
                      target_category,
                      activations,
                      grads,
                      eigen_smooth):
        return get_2d_projection(grads * activations)