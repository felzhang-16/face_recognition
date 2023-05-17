const getConfiguration = () => {
    const sourceDir = document.getElementById('input-source-dir');
    const destinationDir = document.getElementById('input-destination-dir');
    const compareName = document.getElementById('input-compare-name')
    const compareImage = document.getElementById('input-compare-image')
    config = {
        sourceDir: sourceDir.value,
        destinationDir: destinationDir.value,
        compare: { name: compareName.value, image: compareImage.value }
    };
    return config;
}