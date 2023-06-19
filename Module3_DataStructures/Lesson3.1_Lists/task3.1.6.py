
deals = [
    'погулять с друзьями',
    'почитать новости про политику и сцепиться с кем-нибудь в комментах',
    'почитать книжку',
    'заплевать потолок',
    'поиграть в Brawl stars',
    'помыть посуду',
    'сказать родителям, что заболел',
    'залипнуть в летсплеи по роблоксу',
    'покормить кота'
]

new_deals = []

for deal in deals:
  isDone = input(f'{deal} - сделано?: ')
  if isDone == 'да':
    new_deals.append(f'{deal} - сделано')
  else:
    new_deals.append(f'{deal} - не сделано')

for deal in new_deals:
  print(deal)