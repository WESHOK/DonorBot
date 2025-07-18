from datetime import date
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Donor
from .abstract import Repository


class DonorRepo(Repository[Donor]):
    '''quiz_user repository for CRUD and other SQL queries.'''

    def __init__(self, session: AsyncSession):
        '''Initialize user repository as for all users or only for one user.'''

        super().__init__(type_model=Donor, session=session)

    async def new(
        self,
        fio: str,
        group: str,
        gavrilov_amount: int,
        fmba_amount: int,
        sum: int,
        gavrilov_last_donation_date: date,
        fmba_last_donation_date: date,
        social_contacts: str,
        number: str,
    ):
        '''Insert a new quiz_user into the database.'''

        await self.session.merge(
            Donor(
                fio=fio,
                group=group,
                gavrilov_amount=gavrilov_amount,
                fmba_amount=fmba_amount,
                sum=sum,
                gavrilov_last_donation_date=gavrilov_last_donation_date,
                fmba_last_donation_date=fmba_last_donation_date,
                social_contacts=social_contacts,
                number=number,
            )
        )

        await self.session.commit()

    async def from_dict(self, data: dict):
        '''Wrapper for 'new' method.'''

        await self.new(
            data['fio'],
            data['group'],
            data['gavrilov_amount'],
            data['fmba_amount'],
            data['sum'],
            data['gavrilov_last_donation_date'],
            data['fmba_last_donation_date'],
            data['social_contacts'],
            data['number'],
        )