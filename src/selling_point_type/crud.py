from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from selling_point_type.models import SellingPointType
from selling_point_type.schemas import SellingPointTypeCreate, SellingPointTypeUpdate

from core.base_crud import CRUDBase


class CrudSellingPointType(CRUDBase[SellingPointType, SellingPointTypeCreate, SellingPointTypeUpdate]):

    async def get_selling_point_type_by_id(self, *, db: AsyncSession, selling_point_type_id: int):
        selling_point_type = await self.get(db=db, id=selling_point_type_id)
        if selling_point_type is None:
            return None, -2, None
        return selling_point_type, 0, None

    async def get_all_selling_point_types(self, *, db: AsyncSession, skip: int, limit: int):
        selling_point_types = await self.get_multi(db_session=db, skip=skip, limit=limit)
        return selling_point_types, 0, None

    async def create_selling_point_type(self, *, db: AsyncSession, new_data: SellingPointTypeCreate):
        # check by id
        query = select(self.model).where(self.model.id == new_data.id)
        response = await db.execute(query)
        if response.scalar_one_or_none() is not None:
            return None, -3, None
        new_selling_point_type = await self.create(db_session=db, obj_in=new_data)
        return new_selling_point_type, 0, None

    async def update_selling_point_type(self,
                                        *,
                                        db: AsyncSession,
                                        update_data: SellingPointTypeUpdate,
                                        selling_point_type_id: int):
        # check by id
        query = select(self.model).where(self.model.id == selling_point_type_id)
        response = await db.execute(query)
        current_selling_point_type = response.scalar_one_or_none()
        if current_selling_point_type is None:
            return None, -3, None
        updated_selling_point_type = await self.update(db_session=db,
                                                  obj_current=current_selling_point_type,
                                                  obj_new=update_data)
        return updated_selling_point_type, 0, None

    async def delete_selling_point_type(self, *, db: AsyncSession, selling_point_type_id: int):
        # check id
        query = select(self.model).where(self.model.id == selling_point_type_id)
        response = await db.execute(query)
        current_selling_point_type = response.scalar_one_or_none()
        if current_selling_point_type is None:
            return None, -3, None
        deleted_selling_point_type = await self.delete(db=db, id=selling_point_type_id)
        return deleted_selling_point_type, 0, None


crud_selling_point_type = CrudSellingPointType(SellingPointType)