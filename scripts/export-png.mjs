import { readFileSync, writeFileSync } from 'node:fs';
import { Resvg } from '@resvg/resvg-js';

const svgPath = '/workspace/assets/kiyaf-snap-poster.svg';
const outPath = '/workspace/assets/kiyaf-snap-poster-1080x1920.png';

const svg = readFileSync(svgPath, 'utf8');

const fontFiles = [
	'/workspace/assets/fonts/Tajawal-Bold.ttf',
	'/workspace/assets/fonts/Tajawal-Medium.ttf',
	'/workspace/assets/fonts/NotoKufiArabic-Regular.ttf',
	'/workspace/assets/fonts/NotoKufiArabic-SemiBold.ttf'
];

const resvg = new Resvg(svg, {
	fitTo: { mode: 'original' },
	background: 'white',
	font: {
		loadSystemFonts: false,
		defaultFontFamily: 'Tajawal',
		fontFiles
	}
});

const pngData = resvg.render();
const pngBuffer = pngData.asPng();
writeFileSync(outPath, pngBuffer);

console.log('Exported', outPath);