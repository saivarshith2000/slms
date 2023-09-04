import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/shadcnui/ui/table'
import { Avatar, AvatarFallback } from '@/shadcnui/ui/avatar'
import { DotsHorizontalIcon } from '@radix-ui/react-icons'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/shadcnui/ui/dropdown-menu'
import { Button } from '@/shadcnui/ui/button'

import { UserAccount } from '../types'
import RoleBadge from './RoleBadge'
import ActiveBadge from './ActiveBadge'
import { formatDateTime } from '@/lib/date'

type UserAccountsTableProps = {
  users: UserAccount[]
}

export function UserActionsMenu({ user }: { user: UserAccount }) {
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant='ghost'>
          <DotsHorizontalIcon />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent>
        {!user.active && <DropdownMenuItem>Activate</DropdownMenuItem>}
        {user.active && <DropdownMenuItem>Deactivate</DropdownMenuItem>}
        <DropdownMenuItem>Profile</DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}

function Row({ user }: { user: UserAccount }) {
  const { date, time } = formatDateTime(new Date(user.created_at))
  const abbr = user.first_name[0].toUpperCase() + user.last_name[0].toUpperCase()

  return (
    <TableRow key={user.email}>
      <TableCell className='flex items-center space-x-3'>
        <Avatar className='h-[32px] w-[32px]'>
          <AvatarFallback>{abbr}</AvatarFallback>
        </Avatar>
        <p>
          {user.first_name}, {user.last_name}
        </p>
      </TableCell>
      <TableCell>{user.email}</TableCell>
      <TableCell>
        <RoleBadge role={user.role} />
      </TableCell>
      <TableCell>
        <ActiveBadge active={user.active} />
      </TableCell>
      <TableCell>
        {time} &nbsp; {date}
      </TableCell>
      <TableCell className='max-w-[40px]'>
        <UserActionsMenu user={user} />
      </TableCell>
    </TableRow>
  )
}

export function UserAccountsTable({ users }: UserAccountsTableProps) {
  users.forEach((u) => console.log(new Date(u.created_at)))

  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead className='max-w-[250px]'>Name</TableHead>
          <TableHead>Email</TableHead>
          <TableHead>Role</TableHead>
          <TableHead>Active</TableHead>
          <TableHead>Created At</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {users.map((u) => (
          <Row user={u} key={u.email} />
        ))}
      </TableBody>
    </Table>
  )
}
