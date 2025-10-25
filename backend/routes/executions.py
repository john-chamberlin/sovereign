from fastapi import APIRouter

router = APIRouter(prefix='/api/executions', tags=['executions'])


@router.get('/')
def list_executions():
    
    return [{'id': 1, 'workflow_id': 1, 'status': 'SUCCESS'}]

@router.get('/{execution_id}')
def get_execution(execution_id: int):
    
    return {
        'id': execution_id,
        'workflow_id': 1,
        'status': 'SUCCESS',
        'result': {'actions': []}
    }