def write(game):
    output = (
        f"\033[HWidth in columns: {game.size.columns}\n" +
        f"Height in rows: {game.size.lines}\n"
    )
    return output