"""merge all heads

Revision ID: 9b3050409b66
Revises: ca4c4abcc347, 69761b1b5e9a, 4474872b0ee6
Create Date: 2025-06-11 10:45:51.392388

"""
from alembic import op
import models as models
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b3050409b66'
down_revision = ('ca4c4abcc347', '69761b1b5e9a', '4474872b0ee6')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
