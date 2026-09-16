from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page
from shadcn.plugins.mixins.git import GitTimestampsMixin


def _skip_git_for_generated_pages(
    self: GitTimestampsMixin,
    markdown: str,
    /,
    *,
    page: Page,
    config: MkDocsConfig,
    files: Files,
) -> str:
    if getattr(page.file, "generated_by", None):
        return super(GitTimestampsMixin, self).on_page_markdown(
            markdown,
            page=page,
            config=config,
            files=files,
        )

    return GitTimestampsMixin.on_page_markdown(
        self,
        markdown,
        page=page,
        config=config,
        files=files,
    )


def on_config(config: MkDocsConfig) -> MkDocsConfig:
    # Shadcn theme asks Git for history of AutoAPI's temporary files, which
    # fails. Therefore, force skip that when running over these auto generated
    # files.
    GitTimestampsMixin.on_page_markdown = _skip_git_for_generated_pages
    return config
