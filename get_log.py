from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
with api.build_kaggle_client() as kaggle:
    from kagglesdk.kernels.types.kernels_api_service import (
        ApiListKernelSessionOutputRequest,
    )

    req = ApiListKernelSessionOutputRequest()
    req.user_name = "dzackgarza"
    req.kernel_slug = "vakil-test-5pages-mineru-job-20260323221209"
    resp = kaggle.kernels.kernels_api_client.list_kernel_session_output(req)
    with open("kernel_log.txt", "w") as f:
        f.write(resp.log or "NO LOG")
print("Done")
