import React from 'react'

function useForm( initialFormState = {}, submitFunction, submitParams = null, onSubmitSuccess = () => {} ) {

  // * Initial state 
  const [formData, setFormData] = React.useState(initialFormState)
  const [formErrors, setFormErrors] = React.useState(initialFormState)


  //* HandleChange event for inputting values on form & sets them and the errors to state 
  const handleChange = ({ target: { name, value, type, checked } }) => {
    const newValue = type === 'checkbox' ? checked : value
    const updatedFormData = { ...formData, [name]: newValue }
    const updatedErrors = { ...formErrors, [name]: '' }
  
    setFormData(updatedFormData)
    setFormErrors(updatedErrors)
  }

  console.log(formData)


  // * Handle submit function, on submitSuccess passed in as params 
  const handleSubmit = async event => {
    event.preventDefault()    
    
    try {
      const response = await submitFunction(formData, submitParams)
      onSubmitSuccess(response)
    } catch (err) {
      console.log('response err', err)
      // setFormErrors(err.response.data.errors)
    }
  }
  
  return { formData, handleChange, setFormData, formErrors, setFormErrors, handleSubmit }
}
export default useForm