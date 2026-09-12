from fastapi import APIRouter

router = APIRouter()

@router.get('/api/test')
def return_test():
    return 'test is working'


