function sendMail(contactForm) {
  emailjs.send('gmail', 'cookbook', {
    'from_name': contactForm.name.value,
    'from_email': contactForm.email.value,
    'cookbook_message': contactForm.message.value
  })
    .then(
      function (response) {
        console.log('SUCCESS', response);
      },
      function (error) {
        console.log('FAILED', error);
      }
    )
  return false;
}
