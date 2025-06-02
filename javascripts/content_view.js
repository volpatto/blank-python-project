// Based on this discussion:
// https://github.com/squidfunk/mkdocs-material/discussions/6850
"use strict";

window.addEventListener("DOMContentLoaded", _ => {
    myModifyViewPageButtonToBlob();
});

const myModifyViewPageButtonToBlob = () => {
    for (const anchor of document.querySelectorAll("a.md-content__button")) {
        anchor.href = anchor.href.replace("/raw/main/", "/blob/main/");
    }
};
