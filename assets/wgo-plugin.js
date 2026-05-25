window.onload = function() {
	document.querySelectorAll('a[href$=".sgf"]').forEach(link => {
		const sgfFile = link.getAttribute('href');
		const details = document.createElement('details');
		const summary = document.createElement('summary');
		const content = document.createElement('div');
		summary.textContent = 'replay ' + sgfFile;

		details.appendChild(summary);
		details.appendChild(content);
		link.insertAdjacentElement('afterend', details);

		new WGo.BasicPlayer(content, {
			sgfFile: sgfFile,
			board: {
				// NORMAL PAINTED GLOW SHELL MONO
				stoneHandler: WGo.Board.drawHandlers.PAINTED
			}
		});
	});
}
