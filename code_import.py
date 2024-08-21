from main.models import Lottery

lottery_configs = [
    {'code_mask': 'ITC11{:03d}', 'code_range': 260, 'description': "Мега"},
    {'code_mask': 'ITC12{:03d}', 'code_range': 250, 'description': "Молл"},
    {'code_mask': 'ITC13{:03d}', 'code_range': 180, 'description': "Мега-2"},
    {'code_mask': 'ITC14{:03d}', 'code_range': 60, 'description': "100 айл"},
    {'code_mask': 'ITC15{:03d}', 'code_range': 60, 'description': "Дархан"},
    {'code_mask': 'ITC16{:03d}', 'code_range': 40, 'description': "Эрдэнэт"},
    {'code_mask': 'ITC17{:03d}', 'code_range': 25, 'description': "Өмнөговь"},
    {'code_mask': 'ITC18{:03d}', 'code_range': 25, 'description': "Интернет"},
    {'code_mask': 'ITC19{:03d}', 'code_range': 20, 'description': "Гэрээт"}
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