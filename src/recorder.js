
// Gravador de áudio (browser) usando MediaRecorder API
// Exporta função record(ms) que resolve com Data URL base64

const sleep = (time) => new Promise((resolve) => setTimeout(resolve, time));

const blobToDataURL = (blob) => new Promise((resolve) => {
  const reader = new FileReader();
  reader.onloadend = (e) => resolve(e.srcElement.result);
  reader.readAsDataURL(blob);
});

export async function record(ms = 5000) {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  const recorder = new MediaRecorder(stream);
  const chunks = [];

  recorder.ondataavailable = (e) => chunks.push(e.data);
  recorder.start();
  await sleep(ms);

  return await new Promise((resolve) => {
    recorder.onstop = async () => {
      const blob = new Blob(chunks, { type: 'audio/wav' });
      const dataURL = await blobToDataURL(blob);
      resolve(dataURL);
      stream.getTracks().forEach((t) => t.stop());
    };
    recorder.stop();
  });
}
