from fastapi import APIRouter

router = APIRouter(prefix='/api/integrations', tags=['integrations'])


@router.get('/')
def list_integrations():
    
    return [{'name': 'discord', 'status': 'connected'},{'name': 'slack', 'status': 'connected'} ]