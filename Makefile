TWINE_REPOSITORY ?= pypi.syslab.com

.PHONY: release
release:
	@echo "Releasing to $(TWINE_REPOSITORY)"
	@echo 'run `make release TWINE_REPOSITORY=<name>` to override'
	TWINE_REPOSITORY=$(TWINE_REPOSITORY) uvx \
	--from zest-releaser \
	--with zest-releaser'[recommended]' \
	--with zestreleaser-towncrier fullrelease
