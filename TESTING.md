# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| File | screenshot | Notes |                                                                                                 |
| --- | --- | --- | ----------------------------------------------------------------------------------------------------------|
| index.html | ![screenshot](assets/images/html-validation.webp) | Pass: No Errors |
| 404.html | ![screenshot](assets/images/404-html-validation.webp) | Pass: No Errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | screenshot | Notes |                                                                                                 |
| --- | --- | --- | ----------------------------------------------------------------------------------------------------------|
| style.css  | ![screenshot](static/images/css-validation.webp) |  Pass: No Errors |



### WAVE Web Accessibility Evaluation Tool

I've also tested my deployed project on WAVE Web Accessibility Evaluation Tool to check for any issues.

| Browser | Summary | Details | Structure | Contrast | Homepage | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](static/images/wave-home-summary-page.webp) | ![screenshot](static/images/wave-home-details-page.webp) | ![screenshot](static/images/wave-home-structure-page.webp) | ![screenshot](static/images/wave-home-contrast-page.webp) | ![screenshot](static/images/wave-home-landing-page.webp) | Pass: No Errors |
| |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Notes |  |
| --- | --- | --- | --- | 
| Chrome | ![screenshot](static/images/chrome-home-page.webp) | Works as expected |
| Firefox | ![screenshot](static/images/firefox-home-page.webp) | Works as expected |
| Safari | ![screenshot](static/images/safari-home-page.webp) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- | 
| Home | ![screenshot](assets/images/lhs-mobile.webp) | ![screenshot](assets/images/lhs-desktop.webp) | Warnings: Resource are blocking the first paint of your page and error logged to console due to network request failure. |
| 404 error page | ![screenshot](assets/images/404-lhs-mobile.webp) | ![screenshot](assets/images/404-lhs-desktop.webp) | Lighthouse was unable to reliably load the page you requested. Make sure you are testing the correct URL and that the server is properly responding to all requests. (Status code: 404) |

## Responsiveness

I've tested my deployed project for responsiveness issues.

| Device | Home | Notes |  |
| --- | --- | --- | --- | 
| Mobile (DevTools) | ![screenshot](static/images/mobile.webp) | Works as expected | 
| Tablet (DevTools) | ![screenshot](static/images/tablet.webp) | Works as expected |
| Desktop (DevTools) | ![screenshot](static/images/laptop.webp) | Works as expected |


> [!NOTE]  
> Return back to the [README.md](README.md) file.