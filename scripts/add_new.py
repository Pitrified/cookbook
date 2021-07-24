"""Create placeholder posts for new recipes."""
import argparse
from datetime import datetime
import logging
from pathlib import Path
import shutil


def parse_arguments() -> argparse.Namespace:
    r"""Setup CLI interface.

    Returns:
        The parsed arguments.
    """
    parser = argparse.ArgumentParser(description="")

    default = "WARN"
    parser.add_argument(
        "--console_log_level",
        type=str,
        default=default,
        help=f"Level for the console logger, default {default}",
        choices=["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"],
    )

    default = "lnm"
    parser.add_argument(
        "--console_fmt_type",
        type=str,
        default=default,
        help=f"Message format for the console logger, default {default}",
        choices=["lanm", "lnm", "lm", "nm", "m"],
    )

    # last line to parse the args
    args = parser.parse_args()
    return args


def setup_logger(
    console_fmt_type: str = "m",
    console_log_level: str = "WARN",
) -> None:
    r"""Setup loggers for the module.

    Args:
        console_fmt_type: Message format for the console logger.
        console_log_level: Logger level for the console logger.
    """
    # setup the format strings
    format_types = {}
    format_types["lanm"] = "[%(levelname)-8s] %(asctime)s %(name)s: %(message)s"
    format_types["lnm"] = "[%(levelname)-8s] %(name)s: %(message)s"
    format_types["lm"] = "[%(levelname)-8s]: %(message)s"
    format_types["nm"] = "%(name)s: %(message)s"
    format_types["m"] = "%(message)s"

    # setup the console handler with the console formatter
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(format_types[console_fmt_type])
    console_handler.setFormatter(console_formatter)

    # setup the console logger with the console handler
    logconsole = logging.getLogger("c")
    logconsole.propagate = False
    logconsole.setLevel(console_log_level)
    logconsole.addHandler(console_handler)


def setup_env() -> argparse.Namespace:
    r"""Setup the logger and parse the args.

    Returns:
        The parsed arguments.
    """
    # parse the command line arguments
    args = parse_arguments()

    # setup the loggers
    console_fmt_type = args.console_fmt_type
    console_log_level = args.console_log_level
    setup_logger(console_fmt_type=console_fmt_type, console_log_level=console_log_level)

    # build command string to repeat this run, useful to remember default values
    # if an option is a flag this does not work (can't just copy/paste), sorry
    recap = "python3 sample_logger.py"
    for a, v in args._get_kwargs():
        recap += f" --{a} {v}"
    logg = logging.getLogger(f"c.{__name__}.setup_env")
    logg.info(recap)

    return args


def run_add_new(args: argparse.Namespace) -> None:
    r"""Create placeholder posts for new recipes.

    base_new_images
        |==== new
        |   |==== dolci
        |       |==== recipe_name_1
        |           |==== finito.jpg
        |           |==== whatever.jpg
        |==== todo
    cookbook_repo/ghpages
        |==== _posts
        |   |==== dolci
        |       |==== 2021-03-05-recipe_name_1.md
        |==== assets/images
            |==== recipe_name_1
                |==== finito.jpg

    Needs to, if finito is found:
        * Create recipe_name_1 folder in the img directory
        * Copy finito.jpg there
        * Create the category folder if it is the first
        * Create recipe_name_1 folder in the right category for post and todo
        * Create recipe_name_1.md post with date in front, using template
          to fill in the name/category, "Buoni di sicuro" as description
        * Move the folder recipe_name_1 to todo

    TODO:
        * Something should check if a recipe with the same name exists
        * Search for more combinations finito_name.jpeg
        * Cmdline images_base_folder

    Args:
        args: The parsed cmdline arguments.
    """
    logg = logging.getLogger(f"c.{__name__}.run_add_new")
    logg.setLevel("DEBUG")
    logg.debug("Starting run_add_new")


    script_base_folder = Path(__file__).absolute().parent
    logg.debug(f"script_base_folder: {script_base_folder}")
    recipe_template_path = script_base_folder / "recipe_template.txt"
    recipe_template = recipe_template_path.read_text()
    # logg.debug(f"recipe_template: {recipe_template}")

    # repo_base_folder = Path("~/repos/cookbook").expanduser()
    repo_base_folder = script_base_folder.parent
    repo_img_folder = repo_base_folder / "ghpages" / "assets" / "images"

    # images_base_folder = Path("~/ephem/cook_photo/cookbook").expanduser()
    images_base_folder = Path("~/Pictures/ricette").expanduser()
    new_images_folder = images_base_folder / "new"
    todo_base_folder = images_base_folder / "todo"

    for new_images_cat_folder in new_images_folder.iterdir():
        cat_name = new_images_cat_folder.name
        logg.debug(f"cat_name: {cat_name}")

        # create the category folders for post and todo
        todo_cat_folder = todo_base_folder / cat_name
        logg.debug(f"todo_cat_folder: {todo_cat_folder}")
        if not todo_cat_folder.exists():
            todo_cat_folder.mkdir(parents=True)
        repo_cat_folder = repo_base_folder / "ghpages" / "_posts" / cat_name
        logg.debug(f"repo_cat_folder: {repo_cat_folder}")
        if not repo_cat_folder.exists():
            repo_cat_folder.mkdir(parents=True)

        # iterate over the new recipes for this category
        for new_recipe_folder in new_images_cat_folder.iterdir():
            logg.debug(f"new_recipe_folder: {new_recipe_folder}")
            recipe_name = new_recipe_folder.name
            logg.debug(f"recipe_name: {recipe_name}")

            # make the recipe folder in repo_img_folder
            new_recipe_img_folder = repo_img_folder / recipe_name
            logg.debug(f"new_recipe_img_folder: {new_recipe_img_folder}")
            if not new_recipe_img_folder.exists():
                new_recipe_img_folder.mkdir(parents=True)
            else:
                logg.debug(f"Already exists: {new_recipe_img_folder}")

            # TODO should check for jpeg
            finito_name = "finito.jpg"
            finished_img_path = new_recipe_folder / finito_name
            if not finished_img_path.exists():
                continue

            # copy the image
            new_img_path_dst = new_recipe_img_folder / finito_name
            shutil.copy2(finished_img_path, new_img_path_dst)

            # build a readable title for the post
            recipe_title = recipe_name.replace("_", " ")
            recipe_title_up = recipe_title.capitalize()
            logg.debug(f"recipe_title_up: {recipe_title_up}")

            # build the post file name
            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d")
            post_name = f"{date_time}-{recipe_name}.md"
            logg.debug(f"post_name: {post_name}")

            # build the post and save it
            recipe_post = recipe_template.format(
                category=cat_name,
                title_up=recipe_title_up,
                recipe_name=recipe_name,
                finito_name=finito_name,
                title=recipe_title,
            )
            logg.debug(f"recipe_post:\n{recipe_post}")
            post_path = repo_cat_folder / post_name
            logg.debug(f"post_path: {post_path}")
            post_path.write_text(recipe_post)

            # move the new image folder in todo/cat
            shutil.move(str(new_recipe_folder), todo_cat_folder)


if __name__ == "__main__":
    args = setup_env()
    run_add_new(args)
