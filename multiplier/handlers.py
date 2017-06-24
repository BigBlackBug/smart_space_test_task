from aiohttp import web

from multiplier import multiplier_service


async def multiply_matrices(request):
    data = await request.json()
    first = data['first']
    second = data['second']
    job_id = multiplier_service.multiply(first, second)
    return web.json_response({
        "job_id": str(job_id)
    })


async def job_status(request):
    job_id = request.match_info.get('job_id')
    status = multiplier_service.job_status(job_id)
    return web.json_response({
        "status": status
    })


async def get_result(request):
    job_id = request.match_info.get('job_id')
    status, result = multiplier_service.get_result(job_id)
    return web.json_response({
        "status": status,
        "result": result
    })
