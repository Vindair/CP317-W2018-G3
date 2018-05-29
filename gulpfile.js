const fs = require('fs');
const gulp = require('gulp');
const showdown = require('showdown');
const tidy = require('htmltidy2').tidy;

// Task to watch .md files, convert to HTML, then tidy
gulp.task('markdown', () => {
  console.log('Watching Markdown files for changes...');

  gulp.watch('documents/*.md', (status) => {
    const converter = new showdown.Converter();

    if (status.type === 'changed') {
      fs.readFile(status.path, 'utf8', (err, data) => {
        let html = converter.makeHtml(data);

        tidy(html, {indent: true, wrap: 0}, (err, out) => {
          fs.writeFileSync(`${status.path}.html`, out);
        });
      });

      console.log(`Generated: ${status.path}.html`);
    }
  });
});
