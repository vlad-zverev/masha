from .factories import create_beavers_family, create_humans_family, create_other_humans_family
from .party import SwingerParty

beavers_family = create_beavers_family()
humans_family = create_humans_family()
other_humans_family = create_other_humans_family()

party = SwingerParty()

party.join_family(beavers_family)
party.join_family(humans_family)
party.join_family(other_humans_family)

party.start_group_sex()
