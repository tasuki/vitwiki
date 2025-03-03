window.onload = function() {
	document.querySelectorAll('a[href$=".sgf"]').forEach(link => {
		const sgfFile = link.getAttribute('href');
		const details = document.createElement('details');
		const summary = document.createElement('summary');
		const content = document.createElement('div');
		summary.textContent = 'replay ' + sgfFile;
		content.setAttribute('data-wgo', sgfFile);

		details.appendChild(summary);
		details.appendChild(content);
		link.insertAdjacentElement('afterend', details);
	});
}
