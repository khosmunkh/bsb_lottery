from main.models import Lottery

lottery_configs = [
    {'code_mask': 'HOMMOL11{:03d}', 'code_range': 150, 'description': ""},
    {'code_mask': 'HOMSTY12{:03d}', 'code_range': 120, 'description': ""},
    {'code_mask': 'HOMMIS13{:03d}', 'code_range': 100, 'description': ""},
    {'code_mask': 'BSBINT17{:03d}', 'code_range': 60, 'description': ""},
    {'code_mask': 'MEBMOL18{:03d}', 'code_range': 60, 'description': ""},
    {'code_mask': 'MEBOFM19{:03d}', 'code_range': 60, 'description': ""},
    {'code_mask': 'MEBMIS20{:03d}', 'code_range': 60, 'description': ""},
    {'code_mask': 'HOMERD14{:03d}', 'code_range': 60, 'description': ""},
    {'code_mask': 'HOMDAR15{:03d}', 'code_range': 60, 'description': ""},
    {'code_mask': 'HOMUMG16{:03d}', 'code_range': 60, 'description': ""},
]

for config in lottery_configs:
    lotteries = [
        Lottery(
            code=config['code_mask'].format(i),
            description=config['description']
        )
        for i in range(1, config['code_range'] + 1)
    ]
    Lottery.objects.bulk_create(lotteries)