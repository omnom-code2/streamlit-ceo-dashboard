import humanize

def format_metric(value, metric_type):
  if metric_type == "dollars":
    return f'${humanize.metric(value)}'
  elif metric_type == "percent":
    return f'{round(value * 100, 1)}%'
  return f'{value}'
