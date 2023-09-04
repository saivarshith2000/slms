export type UserAccount = {
  first_name: string
  last_name: string
  email: string
  role: 'ADMIN' | 'STUDENT' | 'TEACHER'
  active: boolean
  activated_at: Date | null
  created_at: Date
}
