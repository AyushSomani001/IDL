import numpy as np
from base_cam import BaseCAM
from svd_on_activations import get_2d_projection

class GradCAM(BaseCAM):
    def __init__(self, model, target_layers, use_cuda=False,
                 reshape_transform=None):
        super(
            GradCAM,
            self).__init__(
            model,
            target_layers,
            use_cuda,
            reshape_transform)

    def get_cam_weights(self,
                        input_tensor,
                        target_layer,
                        target_category,
                        activations,
                        grads):
        return np.mean(grads, axis=(2, 3))


class GradCAMElementWise(BaseCAM):
    def __init__(self, model, target_layers, use_cuda=False,
                 reshape_transform=None):
        super(
            GradCAMElementWise,
            self).__init__(
            model,
            target_layers,
            use_cuda,
            reshape_transform)

    def get_cam_image(self,
                      input_tensor,
                      target_layer,
                      target_category,
                      activations,
                      grads,
                      eigen_smooth):
        elementwise_activations = np.maximum(grads * activations, 0)

        if eigen_smooth:
            cam = get_2d_projection(elementwise_activations)
        else:
            cam = elementwise_activations.sum(axis=1)
        return cam

# https://ieeexplore.ieee.org/abstract/document/8354201?casa_token=SkfwLsr8mIQAAAAA:RD1gtQGd6KSMndoPwPJ6VXBickTKN_AxAXWmDReMZeYf5nKP-3e03Tf7WEHzQ3MoGGMzb9_4hOs

class GradCAMPlusPlus(BaseCAM):
    def __init__(self, model, target_layers, use_cuda=False,
                 reshape_transform=None):
        super(GradCAMPlusPlus, self).__init__(model, target_layers, use_cuda,
                                              reshape_transform)

    def get_cam_weights(self,
                        input_tensor,
                        target_layers,
                        target_category,
                        activations,
                        grads):
        grads_power_2 = grads**2
        grads_power_3 = grads_power_2 * grads
        # Equation 19 in https://ieeexplore.ieee.org/abstract/document/8354201?casa_token=SkfwLsr8mIQAAAAA:RD1gtQGd6KSMndoPwPJ6VXBickTKN_AxAXWmDReMZeYf5nKP-3e03Tf7WEHzQ3MoGGMzb9_4hOs
        sum_activations = np.sum(activations, axis=(2, 3))
        eps = 0.000001
        aij = grads_power_2 / (2 * grads_power_2 +
                               sum_activations[:, :, None, None] * grads_power_3 + eps)
        # Now bring back the ReLU from eq.7 in the paper,
        # And zero out aijs where the activations are 0
        aij = np.where(grads != 0, aij, 0)

        weights = np.maximum(grads, 0) * aij
        weights = np.sum(weights, axis=(2, 3))
        return weights
