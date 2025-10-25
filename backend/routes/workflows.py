from fastapi import APIRouter, HTTPException
from typing import Any

router = APIRouter(prefix="/api/workflows", tags=["workflows"])

@router.get('/')
def list_workflows() -> list[dict[str, Any]]:

    return [{"id": 1, "name": "Test Workflow"}]

@router.get('/{workflow_id}')
def get_workflow(workflow_id: int):
    
    if workflow_id == 1:
        return {"id": 1, "name": "Test Workflow", 'actions': []}
    raise HTTPException(status_code=404, detail="Workflow not found")

@router.post('/')
def create_workflow(workflow: dict):
    
    return {'message': 'Workflow created', 'workflow': workflow}

@router.post('/{workflow_id}/run')
def run_workflow(workflow_id: int, payload: dict):
    
    return {
        'message': f'workflow {workflow_id} started',
        'input_payload': payload
    }