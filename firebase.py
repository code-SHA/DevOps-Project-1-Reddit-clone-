data = {
    "functions": {
        "predeploy": [
            "npm --prefix \"$RESOURCE_DIR\" run lint",
            "npm --prefix \"$RESOURCE_DIR\" run build"
        ]
    }
}
