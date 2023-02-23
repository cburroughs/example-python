#Overrides the `image` value for the chart using the target address for the first-party docker image.
helm_deployment(dependencies=["src/chart"],
                sources=["common-values.yaml"],
                values={"image": "src/docker:docker"})
