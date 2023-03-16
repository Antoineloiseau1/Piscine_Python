def ft_tqdm(lst: range) -> None:
    total = len(lst)
    progress = 0
    for item in lst:
        progress += 1
        yield item
        pct_complete = int(progress / total * 100)
        bar_length = 65
        filled_length = int(bar_length * progress / total)
        bar = ('=' * (filled_length - 1)) + ('>' * 1) + \
            ('-' * (bar_length - filled_length))
        completion = str(item + 1) + '/' + str(total)
        print(f'\r{pct_complete}%|[{bar}]| {completion}', end="")
    print()
