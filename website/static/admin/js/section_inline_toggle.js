document.addEventListener('DOMContentLoaded', function () {
    const sectionTypeField = document.querySelector('#id_section_type');
    const projectInline = document.querySelector('#projectitem_set-group');

    function toggleProjectInline() {
        if (sectionTypeField && projectInline) {
            if (sectionTypeField.value === 'projects') {
                projectInline.style.display = 'block';
            } else {
                projectInline.style.display = 'none';
            }
        }
    }

    if (sectionTypeField && projectInline) {
        toggleProjectInline(); // Initial load
        sectionTypeField.addEventListener('change', toggleProjectInline); // On change
    }
});
