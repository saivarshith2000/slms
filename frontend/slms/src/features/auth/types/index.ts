export type SignInInput = {
  email: string
  password: string
}

export type SignInResponse = {
  access_token: string
  user: User
}

export type User = {
  email: string
  first_name: string
  last_name: string
  role: 'STUDENT' | 'TEACHER'
}
