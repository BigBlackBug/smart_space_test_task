from multiplier import handlers

routes = [
    ('POST', '/multiply', handlers.multiply_matrices, 'multiply'),
    ('GET', '/status/{job_id}', handlers.job_status, 'status'),
    ('GET', '/result/{job_id}', handlers.get_result, 'result'),
]
