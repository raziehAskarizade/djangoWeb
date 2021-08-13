const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

const slug = (titleIn) => {
    // way 1:
    titleIn = titleIn.replace(/^\s+|\s+$/g, '');
    titleIn = titleIn.toLowerCase();
    titleIn = titleIn.replace(/[^a-z0-9_\s-ءاأإآؤئبتثجحخدذرزسشصضطظعغفقكلمنهويةى]#u/, '')
        .replace(/\s+/g, '-')
        .replace(/-+/g, '-');
    return titleIn;


    // way 2:
    // return titleIn.toString().trim()
    //     .replace(/&/g, '-and-')
    //     .replace(/[\s\W]+/g, '-')
};

titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slug(titleInput.value));
});